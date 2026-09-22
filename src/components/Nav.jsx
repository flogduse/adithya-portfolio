import { useState } from 'react';
import { profile } from '../data/content';

export default function Nav() {
  const [open, setOpen] = useState(false);

  const close = () => setOpen(false);
  const links = [
    { href: '#work', label: 'WORK' },
    { href: '#building', label: 'BUILDING' },
    { href: '#about', label: 'ABOUT' },
    { href: '#contact', label: 'CONTACT' },
  ];

  return (
    <header className="nav">
      <a className="brand" href="#top" onClick={close}>
        AR<span className="brand-dot">.</span>
      </a>

      <nav className={`nav-links${open ? ' is-open' : ''}`} aria-label="Primary">
        {links.map((l) => (
          <a key={l.href} href={l.href} onClick={close}>
            {l.label}
          </a>
        ))}
      </nav>

      <div className="nav-right">
        <a
          className="btn btn-small nav-cta"
          href={profile.resume}
          target="_blank"
          rel="noreferrer"
        >
          RESUME ↓
        </a>
        <button
          className={`burger${open ? ' is-open' : ''}`}
          onClick={() => setOpen(!open)}
          aria-label={open ? 'Close menu' : 'Open menu'}
          aria-expanded={open}
        >
          <span /><span /><span />
        </button>
      </div>
    </header>
  );
}
