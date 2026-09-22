// ============================================================
//  EDIT THIS FILE to update your portfolio.
//  Every section of the site reads from here — no need to
//  touch any component code for content changes.
// ============================================================

export const profile = {
  name: ['ADITHYA', 'RAJESH'],
  role: 'AI Developer & Engineer',
  roles: ['Machine Learning', 'Computer Vision', 'Robotics', 'Web Systems'],
  location: 'Kollam, Kerala, India',
  degree: "B.Tech CS & AI '29 · CGPA 9.2",
  email: 'adithya.r0987@gmail.com',
  github: 'https://github.com/flogduse',
  linkedin: 'https://www.linkedin.com/in/adithya-rajesh-4486453a2/',
  // TODO: drop your resume PDF at public/resume.pdf to activate the button
  resume: '/resume.pdf',
  bio: "I'm an ML developer crafting intelligent experiences at the intersection of AI, Robotics, and Design. I enjoy turning bold concepts into functional systems — whether that means training models, building interactive web apps, or wiring hardware logic. Code is just another medium for creative expression.",
};

export const stats = [
  { value: '2029', label: 'B.Tech CSE' },
  { value: '4+', label: 'Shipped Projects' },
  { value: '6+', label: 'Tech Domains' },
  { value: '∞', label: 'Curiosity' },
];

export const projects = [
  {
    number: '01',
    title: 'NEXAPATH',
    subtitle: 'AI Career Copilot for Tier-2/3 India',
    description:
      'Built during an IBM SkillsBuild internship. TF-IDF + cosine-similarity job matching, a conversational AI agent, aligned to SDG 4/8/10.',
    tech: ['Python', 'NLP', 'TF-IDF', 'Flask'],
    links: { code: 'https://github.com/flogduse/nexapath', demo: null },
    tag: 'FEATURED',
    accent: 'yellow',
    img: 'https://images.unsplash.com/photo-1620712943543-bcc4688e7485?q=80&w=1600&auto=format&fit=crop',
  },
  {
    number: '02',
    title: 'SYNTH-VISION',
    subtitle: 'Gesture-controlled interfaces',
    description:
      'Real-time spatial tracking with OpenCV and MediaPipe — physics-based UI elements manipulated purely through hand gestures.',
    tech: ['OpenCV', 'MediaPipe', 'Python'],
    links: { code: 'https://github.com/flogduse/second-year', demo: null },
    tag: 'EXPERIMENT',
    accent: 'blue',
    img: 'https://images.unsplash.com/photo-1550751827-4bd374c3f58b?q=80&w=1600&auto=format&fit=crop',
  },
  {
    number: '03',
    title: 'DSA PYTHON',
    subtitle: 'Algorithmic foundations',
    description:
      'A curated collection of data structures, algorithm implementations and Jupyter-based analysis — the core logic layer behind everything else.',
    tech: ['Python', 'DSA', 'Jupyter'],
    links: { code: 'https://github.com/flogduse/dsa-python', demo: null },
    tag: 'COMPUTATION',
    accent: 'red',
    img: 'https://images.unsplash.com/photo-1555066931-4365d14bab8c?q=80&w=1600&auto=format&fit=crop',
  },
  {
    number: '04',
    title: 'COGNITIVE HUB',
    subtitle: 'Backend infrastructure for AI endpoints',
    description:
      'A scalable JavaScript backend architecture engineered to serve and route traffic for intensive AI model endpoints.',
    tech: ['JavaScript', 'Node', 'APIs'],
    links: { code: 'https://github.com/flogduse/first-year', demo: null },
    tag: 'SYSTEM',
    accent: 'yellow',
    img: 'https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=1600&auto=format&fit=crop',
  },
];

// The Phase-1 roadmap — shown as "Currently Building" cards.
// Move a project up into `projects` above once it ships.
export const building = [
  {
    title: 'RAG CAMPUS ASSISTANT',
    description: 'Chat with your syllabus. FastAPI + LangChain + ChromaDB over course PDFs, streaming answers with citations.',
    stack: ['FastAPI', 'LangChain', 'ChromaDB'],
    eta: 'IN PROGRESS',
    accent: 'yellow',
  },
  {
    title: 'GESTURE-CONTROL DESKTOP',
    description: 'Level up Synth-Vision: control volume, scrolling and slides with bare hands via MediaPipe + pynput.',
    stack: ['MediaPipe', 'Python', 'pynput'],
    eta: 'NEXT UP',
    accent: 'blue',
  },
  {
    title: 'SIGN-LANGUAGE TRANSLATOR',
    description: 'Live webcam fingerspelling — MediaPipe keypoints + classifier translating hand signs to text.',
    stack: ['OpenCV', 'LSTM', 'MediaPipe'],
    eta: 'QUEUED',
    accent: 'red',
  },
  {
    title: 'FINE-TUNED MANGLISH LLM',
    description: 'LoRA fine-tune of a compact LLM on Manglish chat data. The stretch goal.',
    stack: ['PEFT', 'LoRA', 'Transformers'],
    eta: 'STRETCH',
    accent: 'yellow',
  },
];

export const skills = [
  {
    category: 'LANGUAGES',
    items: ['Python', 'C / C++', 'JavaScript'],
    level: 'CORE',
    accent: 'yellow',
  },
  {
    category: 'MACHINE LEARNING',
    items: ['Pandas', 'NumPy', 'Scikit-learn', 'Model Training'],
    level: 'LEARNING',
    accent: 'blue',
  },
  {
    category: 'COMPUTER VISION',
    items: ['OpenCV', 'MediaPipe', 'Real-time Tracking'],
    level: 'LEARNING',
    accent: 'red',
  },
  {
    category: 'WEB & BACKEND',
    items: ['Flask', 'Node.js', 'REST APIs'],
    level: 'LEARNING',
    accent: 'yellow',
  },
  {
    category: 'ROBOTICS & HARDWARE',
    items: ['Arduino', 'Sensors', 'Actuator Logic'],
    level: 'CORE',
    accent: 'blue',
  },
  {
    category: 'TOOLING',
    items: ['Git / GitHub', 'Jupyter', 'VS Code'],
    level: 'CORE',
    accent: 'red',
  },
];

export const marqueeItems = [
  'PYTHON', 'MACHINE LEARNING', 'COMPUTER VISION', 'ROBOTICS', 'BACKEND', 'AI', 'OPEN SOURCE',
];
