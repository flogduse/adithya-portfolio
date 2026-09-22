import { useEffect } from 'react';
import { gsap } from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';

gsap.registerPlugin(ScrollTrigger);

export const prefersReducedMotion = () =>
  typeof window !== 'undefined' &&
  window.matchMedia('(prefers-reduced-motion: reduce)').matches;

/**
 * Reveals every element carrying a `data-reveal` attribute as it scrolls
 * into view. The optional attribute value is used as a delay (seconds).
 * Honors prefers-reduced-motion by showing content immediately.
 */
export function useReveal(rootRef) {
  useEffect(() => {
    if (!rootRef.current) return;

    if (prefersReducedMotion()) {
      gsap.set(rootRef.current.querySelectorAll('[data-reveal]'), { clearProps: 'all' });
      return;
    }

    const ctx = gsap.context(() => {
      gsap.utils.toArray('[data-reveal]').forEach((el) => {
        gsap.from(el, {
          y: 36,
          opacity: 0,
          duration: 0.9,
          ease: 'power3.out',
          delay: parseFloat(el.dataset.reveal) || 0,
          scrollTrigger: { trigger: el, start: 'top 88%' },
        });
      });
    }, rootRef);

    return () => ctx.revert();
  }, [rootRef]);
}
