import { profile } from '../data/content';

export default function Contact() {
  return (
    <section className="contact" id="contact">
      <header className="section-header" data-reveal="0">
        <span className="section-kicker">(005) — SAY HELLO</span>
      </header>

      <p className="contact-line" data-reveal="0.05">
        Got an idea, an internship, or just want to talk robots?<br />
        My inbox is open.
      </p>

      <a className="contact-huge" href={`mailto:${profile.email}`} data-reveal="0.1">
        LET'S TALK<span className="accent-dot">.</span>
      </a>

      <div className="contact-links" data-reveal="0.15">
        <a className="btn" href={`mailto:${profile.email}`}>{profile.email}</a>
        <a className="btn" href={profile.github} target="_blank" rel="noreferrer">GITHUB ↗</a>
        <a className="btn" href={profile.linkedin} target="_blank" rel="noreferrer">LINKEDIN ↗</a>
      </div>

      <footer className="footer">
        <span>© 2026 ADITHYA RAJESH</span>
        <span>BUILT LOUD. SHIPPED PROUD.</span>
        <span>KOLLAM, INDIA</span>
      </footer>
    </section>
  );
}
