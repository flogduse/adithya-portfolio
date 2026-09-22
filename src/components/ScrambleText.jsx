import { useEffect, useRef } from 'react';
import { prefersReducedMotion } from './reveal';

const CHARS = '!<>-_\\/[]{}—=+*^?#_';
const FRAMES_PER_CHAR = 4; // ~1 char per 4 frames ≈ 15 chars/sec

export default function ScrambleText({ text, delay = 300 }) {
  const nodeRef = useRef(null);

  useEffect(() => {
    const el = nodeRef.current;
    if (!el) return;

    if (prefersReducedMotion()) {
      el.textContent = text;
      return;
    }

    let raf;
    let frame = 0;
    let done = false;

    const timeout = setTimeout(() => {
      const tick = () => {
        if (done) return;
        frame += 1;
        const revealed = Math.floor(frame / FRAMES_PER_CHAR);
        el.textContent = text
          .split('')
          .map((ch, i) => {
            if (ch === ' ' || i < revealed) return ch;
            return CHARS[Math.floor(Math.random() * CHARS.length)];
          })
          .join('');
        if (revealed < text.length) {
          raf = requestAnimationFrame(tick);
        } else {
          done = true;
        }
      };
      raf = requestAnimationFrame(tick);
    }, delay);

    return () => {
      done = true;
      clearTimeout(timeout);
      cancelAnimationFrame(raf);
    };
  }, [text, delay]);

  return <span ref={nodeRef} className="scramble">{text}</span>;
}
