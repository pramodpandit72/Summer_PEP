"""
extractor.py
------------
Extracts candidate name, skills, and years of experience
from raw resume text using spaCy NLP and regex.
"""

import re
import spacy
from typing import List, Dict, Any

# ---------------------------------------------------------------------------
# Comprehensive skill keyword list
# ---------------------------------------------------------------------------
SKILLS_DB = {
    # Programming Languages
    "python", "java", "javascript", "typescript", "c++", "c#", "c", "go", "golang",
    "rust", "swift", "kotlin", "ruby", "php", "scala", "r", "matlab", "perl",
    "bash", "shell", "powershell", "dart", "lua", "haskell", "elixir", "clojure",

    # Web Frameworks & Libraries
    "react", "reactjs", "angular", "angularjs", "vue", "vuejs", "next.js", "nextjs",
    "nuxt", "svelte", "django", "flask", "fastapi", "express", "expressjs", "spring",
    "spring boot", "laravel", "rails", "ruby on rails", "asp.net", ".net", "blazor",
    "jquery", "bootstrap", "tailwind", "tailwindcss", "material ui",

    # Data Science & ML
    "machine learning", "deep learning", "natural language processing", "nlp",
    "computer vision", "data science", "data analysis", "data engineering",
    "tensorflow", "pytorch", "keras", "scikit-learn", "sklearn", "pandas", "numpy",
    "matplotlib", "seaborn", "plotly", "hugging face", "transformers", "openai",
    "langchain", "llm", "rag", "reinforcement learning", "generative ai",

    # Cloud & DevOps
    "aws", "azure", "gcp", "google cloud", "docker", "kubernetes", "k8s",
    "terraform", "ansible", "jenkins", "ci/cd", "github actions", "gitlab ci",
    "linux", "unix", "nginx", "apache", "heroku", "vercel", "netlify",

    # Databases
    "sql", "mysql", "postgresql", "postgres", "sqlite", "mongodb", "redis",
    "elasticsearch", "cassandra", "dynamodb", "oracle", "mssql", "neo4j",
    "firebase", "supabase", "prisma", "graphql",

    # Tools & Platforms
    "git", "github", "gitlab", "bitbucket", "jira", "confluence", "trello",
    "figma", "photoshop", "illustrator", "canva", "tableau", "power bi",
    "excel", "powerpoint", "word", "jupyter", "vscode", "intellij",

    # Mobile
    "android", "ios", "react native", "flutter", "xamarin", "ionic",

    # Security
    "cybersecurity", "penetration testing", "ethical hacking", "owasp",
    "cryptography", "ssl", "tls", "oauth", "jwt",

    # Soft Skills
    "leadership", "communication", "teamwork", "problem solving", "critical thinking",
    "project management", "agile", "scrum", "kanban", "time management",
    "collaboration", "adaptability", "creativity", "analytical thinking",
    "presentation", "mentoring", "negotiation",

    # Other Technical
    "rest api", "restful", "microservices", "api", "websocket", "grpc",
    "kafka", "rabbitmq", "celery", "spark", "hadoop", "airflow",
    "opencv", "selenium", "playwright", "pytest", "jest", "unit testing",
    "blockchain", "solidity", "web3", "ar", "vr", "iot", "embedded systems",
}

# Experience regex patterns
_EXPERIENCE_PATTERNS = [
    r"(\d+\.?\d*)\s*\+?\s*years?\s+(?:of\s+)?(?:work\s+)?experience",
    r"experience\s+(?:of\s+)?(\d+\.?\d*)\s*\+?\s*years?",
    r"(\d+\.?\d*)\s*\+?\s*yrs?\s+(?:of\s+)?(?:work\s+)?experience",
    r"worked\s+for\s+(?:over\s+)?(\d+\.?\d*)\s*\+?\s*years?",
    r"(\d+\.?\d*)\s*\+?\s*years?\s+(?:of\s+)?industry",
    r"(\d+\.?\d*)\s*\+?\s*years?\s+(?:in\s+)?(?:the\s+)?field",
]

# Date range pattern (e.g., 2019 – 2023, Jan 2020 - Present)
_DATE_RANGE_PATTERN = re.compile(
    r"((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\.?\s+)?"
    r"(20\d{2}|19\d{2})\s*[-–—]\s*"
    r"((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\.?\s+)?"
    r"(20\d{2}|19\d{2}|[Pp]resent|[Cc]urrent|[Nn]ow)",
    re.IGNORECASE,
)


# ---------------------------------------------------------------------------
# Load spaCy model (cached at module level)
# ---------------------------------------------------------------------------
_nlp_model = None


def _get_nlp():
    """Lazily load the spaCy model to avoid slow startup."""
    global _nlp_model
    if _nlp_model is None:
        try:
            _nlp_model = spacy.load("en_core_web_sm")
        except OSError:
            raise RuntimeError(
                "spaCy model 'en_core_web_sm' not found.\n"
                "Run: python -m spacy download en_core_web_sm"
            )
    return _nlp_model


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def extract_name(text: str) -> str:
    """
    Attempt to extract the candidate's name from resume text using spaCy NER.
    Falls back to the first non-empty line if no PERSON entity is found.

    Args:
        text: Raw resume text.

    Returns:
        Candidate name as a string.
    """
    nlp = _get_nlp()
    # Only process the first ~500 chars where the name usually appears
    snippet = text[:500]
    doc = nlp(snippet)

    for ent in doc.ents:
        if ent.label_ == "PERSON":
            name = ent.text.strip()
            # Filter out very short or obviously wrong entities
            if len(name.split()) >= 2 and len(name) < 50:
                return name

    # Fallback: use the first non-empty line
    for line in text.splitlines():
        line = line.strip()
        if line and len(line) < 60 and not any(c.isdigit() for c in line):
            return line

    return "Unknown Candidate"


def extract_skills(text: str) -> List[str]:
    """
    Extract skills from resume text by matching against SKILLS_DB.

    Args:
        text: Raw resume text.

    Returns:
        Sorted list of unique skill names found.
    """
    text_lower = text.lower()
    found_skills = set()

    for skill in SKILLS_DB:
        # Use word-boundary-style matching to avoid partial matches
        pattern = r"(?<![a-zA-Z0-9])" + re.escape(skill) + r"(?![a-zA-Z0-9])"
        if re.search(pattern, text_lower):
            found_skills.add(skill)

    return sorted(found_skills)


def extract_experience(text: str) -> str:
    """
    Extract total years of experience from resume text.
    Uses explicit mention patterns first, then estimates from date ranges.

    Args:
        text: Raw resume text.

    Returns:
        Human-readable string like "3 years" or "5+ years", or "Not specified".
    """
    text_lower = text.lower()

    # 1. Check explicit experience mentions
    for pattern in _EXPERIENCE_PATTERNS:
        match = re.search(pattern, text_lower)
        if match:
            years = float(match.group(1))
            return f"{int(years) if years == int(years) else years} years"

    # 2. Estimate from date ranges
    year_gaps = []
    for match in _DATE_RANGE_PATTERN.finditer(text):
        start_year_str = match.group(2)
        end_year_str = match.group(4)

        try:
            start_year = int(start_year_str)
            if end_year_str.lower() in ("present", "current", "now"):
                import datetime
                end_year = datetime.datetime.now().year
            else:
                end_year = int(end_year_str)

            gap = end_year - start_year
            if 0 < gap <= 50:  # Sanity check
                year_gaps.append(gap)
        except (ValueError, TypeError):
            continue

    if year_gaps:
        total = sum(year_gaps)
        return f"~{total} years (estimated from dates)"

    return "Not specified"


def extract_all(text: str) -> Dict[str, Any]:
    """
    Run all extraction steps on a resume text.

    Args:
        text: Raw text from a PDF resume.

    Returns:
        A dict with keys: name, skills, experience.
    """
    return {
        "name": extract_name(text),
        "skills": extract_skills(text),
        "experience": extract_experience(text),
    }
