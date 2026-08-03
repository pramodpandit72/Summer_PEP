"""
matcher.py
----------
Computes semantic similarity between resume text and a job description
using Sentence-Transformers. Also calculates skill-level matched/missing sets.
"""

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from extractor import extract_skills
from typing import List, Dict, Tuple
import numpy as np

# ---------------------------------------------------------------------------
# Load model once at module level (cached)
# ---------------------------------------------------------------------------
_MODEL_NAME = "all-MiniLM-L6-v2"
_model = None


def _get_model() -> SentenceTransformer:
    """Lazily load the sentence-transformer model."""
    global _model
    if _model is None:
        _model = SentenceTransformer(_MODEL_NAME)
    return _model


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def compute_semantic_score(resume_text: str, jd_text: str) -> float:
    """
    Compute a semantic similarity score between resume and job description.

    Uses cosine similarity on Sentence-Transformer embeddings.

    Args:
        resume_text: Full text of the candidate's resume.
        jd_text:     Full job description text.

    Returns:
        Float score in [0.0, 1.0] representing semantic similarity.
    """
    model = _get_model()
    embeddings = model.encode([resume_text, jd_text], convert_to_numpy=True)
    score = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
    # Clamp to [0, 1] since floating point can drift slightly
    return float(np.clip(score, 0.0, 1.0))


def get_skill_overlap(
    resume_skills: List[str], jd_skills: List[str]
) -> Tuple[List[str], List[str]]:
    """
    Compare resume skills against job description skills.

    Args:
        resume_skills: List of skills extracted from the resume.
        jd_skills:     List of skills extracted from the job description.

    Returns:
        Tuple of (matched_skills, missing_skills).
    """
    resume_set = set(s.lower() for s in resume_skills)
    jd_set = set(s.lower() for s in jd_skills)

    matched = sorted(resume_set & jd_set)
    missing = sorted(jd_set - resume_set)

    return matched, missing


def compute_skill_score(
    resume_skills: List[str], jd_skills: List[str]
) -> float:
    """
    Compute a skill-coverage score as fraction of JD skills present in resume.

    Args:
        resume_skills: Skills found in resume.
        jd_skills:     Skills required by job description.

    Returns:
        Float in [0.0, 1.0]. Returns 0.5 if JD has no extractable skills
        (to avoid penalizing candidates unfairly).
    """
    if not jd_skills:
        return 0.5  # Neutral score when JD has no extractable skills

    resume_set = set(s.lower() for s in resume_skills)
    jd_set = set(s.lower() for s in jd_skills)
    matched_count = len(resume_set & jd_set)

    return matched_count / len(jd_set)


def compute_final_score(
    resume_text: str,
    jd_text: str,
    resume_skills: List[str],
    jd_skills: List[str],
    semantic_weight: float = 0.6,
    skill_weight: float = 0.4,
) -> Dict:
    """
    Compute a blended final match score combining semantic similarity and skill coverage.

    Args:
        resume_text:     Full resume text.
        jd_text:         Full job description text.
        resume_skills:   Skills extracted from resume.
        jd_skills:       Skills extracted from JD.
        semantic_weight: Weight given to semantic similarity (default 0.6).
        skill_weight:    Weight given to skill coverage (default 0.4).

    Returns:
        Dict with keys:
            - match_score (0-100 float)
            - semantic_score (0-100 float)
            - skill_score (0-100 float)
            - matched_skills (list)
            - missing_skills (list)
    """
    semantic = compute_semantic_score(resume_text, jd_text)
    skill_cov = compute_skill_score(resume_skills, jd_skills)
    matched, missing = get_skill_overlap(resume_skills, jd_skills)

    blended = (semantic * semantic_weight) + (skill_cov * skill_weight)
    blended = float(np.clip(blended, 0.0, 1.0))

    return {
        "match_score": round(blended * 100, 2),
        "semantic_score": round(semantic * 100, 2),
        "skill_score": round(skill_cov * 100, 2),
        "matched_skills": matched,
        "missing_skills": missing,
    }
