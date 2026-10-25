// dolavolt – Kontaktformular
// POST /anfrage: prüft die Eingaben und schickt sie als E-Mail an das Team.
// Solange keine E-Mail-Bindung (env.MAIL) eingerichtet ist, bekommt der Besucher
// eine Seite mit vorbereiteter E-Mail, damit keine Anfrage verloren geht.
import { EmailMessage } from "cloudflare:email";

const TO = "hallo@dolavolt.de";
const FROM = "anfrage@dolavolt.de";

const T = {
  de: {
    okT: "Danke für Ihre Anfrage", okP: "Ihre Nachricht ist bei uns angekommen. Sie bekommen innerhalb von zwei Werktagen eine Antwort von einem Ingenieur.",
    back: "Zurück zur Startseite", home: "/",
    errT: "Anfrage unvollständig", errP: "Bitte geben Sie Name, eine gültige E-Mail-Adresse und Ihr Anliegen (mindestens 20 Zeichen) an.",
    fbT: "Fast geschafft", fbP: "Das Formular ist gerade nicht direkt mit unserem Postfach verbunden. Mit einem Klick öffnen Sie eine vorbereitete E-Mail mit Ihrer Anfrage.",
    fbB: "E-Mail mit Anfrage öffnen", subj: "Projektanfrage",
  },
  en: {
    okT: "Thank you for your request", okP: "Your message has reached us. Within two business days you get an answer from an engineer.",
    back: "Back to the homepage", home: "/en/",
    errT: "Request incomplete", errP: "Please enter your name, a valid email address and your request (at least 20 characters).",
    fbT: "Almost done", fbP: "The form is not directly connected to our inbox right now. One click opens a prepared email with your request.",
    fbB: "Open email with request", subj: "Project inquiry",
  },
};

const esc = (s) => s.replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
const clean = (v, max) => String(v ?? "").replace(/\r\n?/g, "\n").trim().slice(0, max);
const oneLine = (s) => s.replace(/[\r\n]+/g, " ");

function page(lang, title, body, status = 200) {
  const t = T[lang];
  const html = `<!doctype html><html lang="${lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>${title} | dolavolt</title><meta name="robots" content="noindex"><link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/assets/styles.css?v=4"></head><body><main id="main"><section class="hero solo"><div class="wrap">
<h1>${title}</h1>${body}<p style="margin-top:32px"><a class="btn quiet" href="${t.home}">${t.back}</a></p></div></section></main></body></html>`;
  return new Response(html, { status, headers: { "content-type": "text/html; charset=utf-8", "cache-control": "no-store" } });
}

function b64utf8(s) {
  const bytes = new TextEncoder().encode(s);
  let bin = "";
  for (const b of bytes) bin += String.fromCharCode(b);
  return btoa(bin).replace(/.{76}/g, "$&\r\n");
}

function mime({ from, to, replyTo, subject, text }) {
  const id = `<${crypto.randomUUID()}@dolavolt.de>`;
  return [
    `From: dolavolt Website <${from}>`,
    `To: ${to}`,
    `Reply-To: ${replyTo}`,
    `Subject: =?UTF-8?B?${b64utf8(subject).replace(/\r\n/g, "")}?=`,
    `Message-ID: ${id}`,
    `Date: ${new Date().toUTCString()}`,
    "MIME-Version: 1.0",
    "Content-Type: text/plain; charset=UTF-8",
    "Content-Transfer-Encoding: base64",
    "",
    b64utf8(text),
  ].join("\r\n");
}

async function handle(request, env) {
  if (request.method !== "POST") return new Response(null, { status: 303, headers: { location: "/#kontakt" } });
  let f;
  try { f = await request.formData(); } catch { return new Response("Bad request", { status: 400 }); }
  const lang = f.get("lang") === "en" ? "en" : "de";
  const t = T[lang];

  // Honeypot: Bots füllen das versteckte Feld aus. Antwort wie bei Erfolg, aber nichts senden.
  if (clean(f.get("website"), 200)) return page(lang, t.okT, `<p class="lead">${t.okP}</p>`);

  const d = {
    name: oneLine(clean(f.get("name"), 120)),
    company: oneLine(clean(f.get("company"), 160)),
    email: oneLine(clean(f.get("email"), 200)),
    phone: oneLine(clean(f.get("phone"), 60)),
    topic: oneLine(clean(f.get("topic"), 120)),
    message: clean(f.get("message"), 5000),
  };
  if (!d.name || !/^[^\s@<>]+@[^\s@<>]+\.[^\s@<>]+$/.test(d.email) || d.message.length < 20)
    return page(lang, t.errT, `<p class="lead">${t.errP}</p>`, 400);

  const subject = `${t.subj}: ${d.topic || "-"} (${d.company || d.name})`;
  const text = `Name: ${d.name}\nUnternehmen: ${d.company || "-"}\nE-Mail: ${d.email}\nTelefon: ${d.phone || "-"}\nThema: ${d.topic || "-"}\nSprache: ${lang}\n\n${d.message}\n`;

  if (env.MAIL) {
    const msg = new EmailMessage(FROM, env.MAIL_TO || TO, mime({ from: FROM, to: env.MAIL_TO || TO, replyTo: d.email, subject, text }));
    try {
      await env.MAIL.send(msg);
      return page(lang, t.okT, `<p class="lead">${t.okP}</p>`);
    } catch (e) {
      console.error("send failed", e);
    }
  }
  // Ausweichweg: vorbereitete E-Mail
  const href = `mailto:${TO}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(text)}`;
  return page(lang, t.fbT, `<p class="lead">${t.fbP}</p><p style="margin-top:24px"><a class="btn" href="${esc(href)}">${t.fbB}</a></p>`);
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (url.pathname === "/anfrage") return handle(request, env);
    return env.ASSETS.fetch(request);
  },
};
