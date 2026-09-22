# ============================================================
#  RESUME DATA — edit this file, then re-run make_resume.py
#  Anything inside [brackets] is a placeholder to replace.
# ============================================================

RESUME = {
    "name": "ADITHYA RAJESH",
    "tagline": "AI / ML Developer · B.Tech CSE '29",
    "location": "Trivandrum, Kerala, India",
    "email": "adithya.0987@gmail.com",
    "github": "github.com/flogduse",
    "linkedin": "linkedin.com/in/adithya-rajesh-4486453a2",

    "summary": (
        "B.Tech Computer Science student (Class of 2029) building intelligent systems "
        "across machine learning, computer vision, robotics and the web. Shipped a "
        "retrieval-augmented chatbot with citations, an NLP career-matching platform "
        "during an IBM internship, and gesture-driven interfaces. Comfortable end-to-end: "
        "data → model → API → interface."
    ),

    "projects": [
        {
            "name": "RAG Campus Assistant",
            "stack": "Python · FastAPI · ChromaDB · sentence-transformers · SSE",
            "bullets": [
                "Retrieval-augmented chatbot that answers campus questions strictly from institutional PDFs, with numbered inline citations.",
                "Built the full pipeline: PDF extraction → overlap chunking → MiniLM embeddings → ChromaDB cosine search → greedy-MMR diversification.",
                "Multi-provider LLM layer (Groq/OpenAI/Ollama) with token-level Server-Sent-Events streaming; retrieval-only fallback mode.",
                "Ships with a 20-test pytest suite covering chunking, metadata coercion and the streaming API contract.",
            ],
        },
        {
            "name": "NexaPath — AI Career Copilot",
            "stack": "Python · NLP · TF-IDF · Flask",
            "bullets": [
                "Career-copilot platform for Tier-2/3 India, built during an IBM SkillsBuild internship.",
                "TF-IDF + cosine-similarity matching engine aligning candidate profiles with opportunities; aligned to SDG 4/8/10.",
            ],
        },
        {
            "name": "Synth-Vision — Gesture Interfaces",
            "stack": "Python · OpenCV · MediaPipe",
            "bullets": [
                "Real-time hand-tracking interface manipulating physics-based UI elements purely through gestures.",
                "Currently expanding into a MediaPipe + pynput desktop control app (volume/scroll/slides).",
            ],
        },
        {
            "name": "DSA Python",
            "stack": "Python · Jupyter",
            "bullets": [
                "Curated data-structures & algorithms collection with Jupyter-based analysis — the foundation layer for all ML work.",
            ],
        },
    ],

    "skills": {
        "Languages": "Python, C/C++, JavaScript",
        "ML / Data": "Pandas, NumPy, scikit-learn, model training & evaluation",
        "Computer Vision": "OpenCV, MediaPipe, real-time tracking",
        "Backend / Web": "FastAPI, Flask, Node.js, REST APIs, SSE streaming",
        "Hardware / Robotics": "Arduino, sensors, actuator logic",
        "Tools": "Git/GitHub, Jupyter, pytest, ChromaDB",
    },

    "education": [
        {
            "degree": "B.Tech, Computer Science and Engineering",
            "school": "TKM College of Engineering, Kollam",
            "meta": "2025 – 2029 (expected) · APJ Abdul Kalam Technological University",
        },
    ],

    "extra": [
        "IBM SkillsBuild internship — AI career-platform track",
        "Build-in-public roadmap: sign-language translator and a LoRA fine-tuned Manglish LLM",
    ],
}
