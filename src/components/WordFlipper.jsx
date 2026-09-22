import { useEffect, useState } from 'react';
import { prefersReducedMotion } from './reveal';

export default function WordFlipper({ words, interval = 2600 }) {
  const [index, setIndex] = useState(0);
  const [paused, setPaused] = useState(false);

  useEffect(() => {
    if (paused || prefersReducedMotion()) return;
    const id = setInterval(() => setIndex((i) => (i + 1) % words.length), interval);
    return () => clearInterval(id);
  }, [paused, interval, words.length]);

  return (
    <span
      className="flip"
      onMouseEnter={() => setPaused(true)}
      onMouseLeave={() => setPaused(false)}
    >
      <span key={index} className="flip-word">{words[index]}</span>
    </span>
  );
}
