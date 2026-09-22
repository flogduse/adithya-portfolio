import { marqueeItems } from '../data/content';
import { prefersReducedMotion } from './reveal';

export default function Marquee() {
  // Reduced motion: static strip instead of the infinite scroll
  if (prefersReducedMotion()) {
    return (
      <div className="marquee marquee-static" aria-hidden="true">
        <div className="marquee-track">
          <span>{marqueeItems.join(' /// ')} ///</span>
        </div>
      </div>
    );
  }

  const row = marqueeItems.map((w) => `${w} /// `).join('');

  return (
    <div className="marquee" aria-hidden="true">
      <div className="marquee-track">
        <span>{row}</span>
        <span>{row}</span>
      </div>
    </div>
  );
}
