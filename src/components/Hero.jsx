import { profile, stats } from '../data/content';
import ScrambleText from './ScrambleText';
import WordFlipper from './WordFlipper';

export default function Hero() {
  return (
    <section className="hero" id="top">
      <div className="hero-ticker" aria-hidden="true">
        <ScrambleText text="AI DEVELOPER & ENGINEER" delay={500} />
      </div>

      <h1 className="hero-name">
        {profile.name.map((line) => (
          <span className="hero-name-line" key={line}>
            <span className="hero-name-text" data-reveal="0">{line}</span>
          </span>
        ))}
      </h1>

      <div className="hero-sub" data-reveal="0.15">
        <span className="hero-flip-label">SPECIALIZING IN</span>
        <span className="hero-flip-wrap"><WordFlipper words={profile.roles} /></span>
      </div>

      <div className="hero-meta" data-reveal="0.3">
        <div className="hero-badges">
          <a className="btn btn-accent" href={profile.github} target="_blank" rel="noreferrer">
            GITHUB ↗
          </a>
          <a className="btn" href="#work">
            SEE THE WORK ↓
          </a>
        </div>
        <div className="hero-loc">
          <span className="dot" aria-hidden="true" />
          {profile.degree} · {profile.location}
        </div>
      </div>

      <ul className="hero-stats" data-reveal="0.4">
        {stats.map((s) => (
          <li key={s.label}>
            <strong>{s.value}</strong>
            <span>{s.label}</span>
          </li>
        ))}
      </ul>
    </section>
  );
}
