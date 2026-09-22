import { profile, projects } from '../data/content';

function ProjectCover({ project }) {
  return (
    <div className={`cover cover-${project.accent}`} aria-hidden="true">
      <span className="cover-title">{project.title}</span>
      <span className="cover-sub">{project.subtitle}</span>
      <span className="cover-badge">{project.tag}</span>
      <span className="cover-num">{project.number}</span>
    </div>
  );
}

export default function Work() {
  return (
    <section className="work" id="work">
      <header className="section-header" data-reveal="0">
        <span className="section-kicker">(002) — SELECTED WORK</span>
        <h2>
          BUILT &<br />SHIPPED<span className="accent-dot">.</span>
        </h2>
      </header>

      <div className="project-list">
        {projects.map((p, i) => {
          const hasRepo = Boolean(p.links?.code);
          const cardInner = (
            <>
              <div className="project-top">
                <span className="project-num">{p.number}</span>
                <span className="project-tag">{p.tag}</span>
              </div>

              <div className="project-cover">
                <ProjectCover project={p} />
              </div>

              <div className="project-body">
                <h3 className="project-title">{p.title}</h3>
                <p className="project-sub">{p.subtitle}</p>
                <p className="project-desc">{p.description}</p>

                <ul className="tech-list" aria-label="Technologies used">
                  {p.tech.map((t) => (
                    <li key={t}>{t}</li>
                  ))}
                </ul>

                <div className="project-links">
                  {hasRepo && (
                    <a
                      className="btn btn-small"
                      href={p.links.code}
                      target="_blank"
                      rel="noreferrer"
                      onClick={(e) => e.stopPropagation()}
                    >
                      CODE ↗
                    </a>
                  )}
                  {p.links?.demo && (
                    <a
                      className="btn btn-small btn-accent"
                      href={p.links.demo}
                      target="_blank"
                      rel="noreferrer"
                      onClick={(e) => e.stopPropagation()}
                    >
                      LIVE DEMO ↗
                    </a>
                  )}
                </div>
              </div>
            </>
          );

          return hasRepo ? (
            <a
              className="project-card"
              key={p.number}
              href={p.links.code}
              target="_blank"
              rel="noreferrer"
              data-reveal={String((i % 2) * 0.1)}
            >
              {cardInner}
            </a>
          ) : (
            <div className="project-card" key={p.number} data-reveal={String((i % 2) * 0.1)}>
              {cardInner}
            </div>
          );
        })}
      </div>

      <p className="work-more" data-reveal="0">
        More experiments live in the repos —{' '}
        <a href={profile.github} target="_blank" rel="noreferrer">
          github.com/flogduse ↗
        </a>
      </p>
    </section>
  );
}
