import { building } from '../data/content';

export default function Building() {
  return (
    <section className="building" id="building">
      <header className="section-header" data-reveal="0">
        <span className="section-kicker">(003) — ON THE BENCH</span>
        <h2>
          CURRENTLY<br />BUILDING<span className="accent-dot">.</span>
        </h2>
      </header>

      <p className="building-intro" data-reveal="0.1">
        An honest look at the workbench. Each of these becomes a full case study
        here the day it ships — built in public, no vaporware.
      </p>

      <div className="building-grid">
        {building.map((b, i) => (
          <article className={`build-card build-${b.accent}`} key={b.title} data-reveal={String((i % 2) * 0.1)}>
            <div className="build-top">
              <span className="build-eta">{b.eta}</span>
              <span className="build-num">{String(i + 1).padStart(2, '0')}</span>
            </div>
            <h3 className="build-title">{b.title}</h3>
            <p className="build-desc">{b.description}</p>
            <ul className="tech-list" aria-label="Stack">
              {b.stack.map((t) => (
                <li key={t}>{t}</li>
              ))}
            </ul>
          </article>
        ))}
      </div>
    </section>
  );
}
