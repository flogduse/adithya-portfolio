import { profile, skills } from '../data/content';
import ScrambleText from './ScrambleText';

export default function About() {
  return (
    <section className="about" id="about">
      <header className="section-header" data-reveal="0">
        <span className="section-kicker">(004) — WHO'S WRITING</span>
        <h2>
          CURIOUS<br />MIND<span className="accent-dot">.</span>
        </h2>
      </header>

      <div className="about-cols">
        <p className="about-bio" data-reveal="0.05">
          {profile.bio}
        </p>

        <div className="skills" data-reveal="0.1">
          {skills.map((group) => (
            <div className={`skill-card skill-${group.accent}`} key={group.category}>
              <div className="skill-head">
                <ScrambleText text={group.category} delay={150} />
                <span className={`badge badge-${group.level === 'CORE' ? 'core' : 'learning'}`}>
                  {group.level}
                </span>
              </div>
              <ul className="skill-items">
                {group.items.map((item) => (
                  <li key={item}>{item}</li>
                ))}
              </ul>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
