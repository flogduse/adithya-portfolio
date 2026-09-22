# ============================================================
#  RESUME DATA — edit this file, then re-run make_resume.py
#  Modeled on the reference DOCX (July 2026) + flagship projects.
#  Anything inside [brackets] is a placeholder to replace.
# ============================================================

RESUME = {
    "name": "ADITHYA RAJESH",
    "tagline": "AI / ML Developer · B.Tech Computer Science with AI · CGPA 9.2",
    "location": "Kollam, Kerala, India",
    "email": "adithya.r0987@gmail.com",
    "phone": "+91 9860698765",
    "github": "github.com/flogduse",
    "linkedin": "linkedin.com/in/adithya-rajesh-4486453a2",
    # TODO: paste your Credly profile URL to show it in the header
    "credly": "",

    # Optional: set to a company name (e.g. "Allianz Technology") when
    # tailoring for a specific application; leave empty for the master copy.
    "target": "",

    "summary": (
        "Second-year B.Tech student in Computer Science with Artificial Intelligence, "
        "seeking a Data Science / AI-ML internship to apply Python-based data analysis "
        "and machine learning fundamentals to real-world business problems while growing "
        "as an engineer. Shipped a retrieval-augmented chatbot with citations and an NLP "
        "career-matching platform during an IBM internship."
    ),

    "education": [
        {
            "degree": "B.Tech in Computer Science with Artificial Intelligence",
            "school": "TKM College of Engineering, Kollam (APJ Abdul Kalam Technological University)",
            "grade": "CGPA: 9.2",
            "meta": "2025 – 2029 (Expected)",
            "lines": [],
        },
        {
            "degree": "Class XII (CBSE)",
            "school": "Loyola School",
            "grade": "94%",
            "meta": "2025",
        },
        {
            "degree": "Class X (CBSE)",
            "school": "RMD International School",
            "grade": "90%",
            "meta": "2023",
        },
    ],

    "experience": [
        {
            "role": "IBM SkillsBuild Academic Internship — AI Automation & Intelligent Solutions",
            "org": "6-week Virtual Internship (Ongoing)",
            "meta": "2026 – Present",
            "bullets": [
                "Undertaking a structured 6-week virtual program on AI automation and intelligent solutions, covering practical applications of AI concepts and tools.",
                "Building NexaPath, an AI career-copilot for Tier-2/3 India, applying program concepts to a production-style codebase.",
            ],
        },
    ],

    "projects": [
        {
            "name": "RAG Campus Assistant",
            "stack": "Python · FastAPI · ChromaDB · sentence-transformers · SSE",
            "bullets": [
                "Retrieval-augmented chatbot answering campus questions strictly from institutional PDFs, with numbered inline citations.",
                "Full pipeline: PDF extraction → overlap chunking → MiniLM embeddings → cosine search → greedy-MMR diversification; token-level streaming via Server-Sent Events.",
                "Pluggable LLM layer (Groq / OpenAI / Ollama) with retrieval-only fallback; ships with a 20-test pytest suite.",
            ],
        },
        {
            "name": "NexaPath — AI Career Copilot",
            "stack": "Python · NLP · TF-IDF · Flask",
            "bullets": [
                "Career-copilot platform for Tier-2/3 India built during the IBM SkillsBuild internship; TF-IDF + cosine-similarity matching aligned to SDG 4/8/10.",
            ],
        },
        {
            "name": "Synth-Vision — Gesture Interfaces",
            "stack": "Python · OpenCV · MediaPipe",
            "bullets": [
                "Real-time hand-tracking interface manipulating physics-based UI elements purely through gestures; expanding into a MediaPipe + pynput desktop-control app.",
            ],
        },
        {
            "name": "Early Python Builds",
            "stack": "Python",
            "bullets": [
                "Console games (Hangman, Quiz, Number Guessing), a to-do list app with file handling, and a CLI calculator with input validation — the foundation layer of my Python fundamentals.",
            ],
        },
    ],

    "skills": {
        "Languages": "Python, C/C++, JavaScript",
        "Libraries / Data": "Pandas, NumPy, Matplotlib, scikit-learn",
        "Core Concepts": "Data Structures & Algorithms, Data Analysis, ML fundamentals",
        "Computer Vision": "OpenCV, MediaPipe, real-time tracking",
        "Backend / Web": "FastAPI, Flask, Node.js, REST APIs, SSE streaming",
        "Tools": "Git/GitHub, Jupyter, pytest, ChromaDB, Arduino",
    },

    "certifications": [
        "Programming, Data Structures and Algorithms using Python — NPTEL, IIT Madras",
        "AI Automation & Intelligent Solutions — IBM SkillsBuild Academic Internship",
        "Getting Started with Generative AI — Credly Verified Badge",
        "Make Agentic AI Work for You — Credly Verified Badge",
    ],
}
