import { useRef } from 'react';
import { createRoot } from 'react-dom/client';
import Nav from './components/Nav';
import Hero from './components/Hero';
import Work from './components/Work';
import Building from './components/Building';
import Marquee from './components/Marquee';
import About from './components/About';
import Contact from './components/Contact';
import { useReveal } from './components/reveal';
import './styles.css';

export default function App() {
  const root = useRef(null);
  useReveal(root);

  return (
    <div ref={root} className="site">
      <Nav />
      <main>
        <Hero />
        <Work />
        <Marquee />
        <Building />
        <About />
        <Contact />
      </main>
    </div>
  );
}

createRoot(document.getElementById('root')).render(<App />);
