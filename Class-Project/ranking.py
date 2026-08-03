"""
ranking.py
----------
Ranks candidates by their match scores.
Uses MinMaxScaler from scikit-learn to normalize scores if needed,
then assigns ranks in descending order of match score.
"""

from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np
from typing import List, Dict, Any


def rank_candidates(candidates: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Sort and rank a list of candidate result dicts by match_score (descending).

    Optionally applies MinMaxScaler normalization when scores are tightly clustered
    (max - min < 5) to spread them out for visual differentiation.

    Args:
        candidates: List of dicts, each containing at minimum:
                    - name (str)
                    - match_score (float, 0-100)
                    - semantic_score (float)
                    - skill_score (float)
                    - matched_skills (list)
                    - missing_skills (list)
                    - skills (list)
                    - experience (str)

    Returns:
        The same list enriched with a 'rank' key (1-indexed), sorted descending.
    """
    if not candidates:
        return []

    scores = np.array([c["match_score"] for c in candidates]).reshape(-1, 1)

    # Normalize only when scores are tightly clustered (< 5 point spread)
    score_range = scores.max() - scores.min()
    if score_range < 5.0 and len(candidates) > 1:
        scaler = MinMaxScaler(feature_range=(30, 95))
        normalized = scaler.fit_transform(scores).flatten()
        for i, candidate in enumerate(candidates):
            candidate["display_score"] = round(float(normalized[i]), 2)
    else:
        for candidate in candidates:
            candidate["display_score"] = candidate["match_score"]

    # Sort descending by original match_score (deterministic ordering)
    sorted_candidates = sorted(candidates, key=lambda c: c["match_score"], reverse=True)

    # Assign ranks
    for rank_idx, candidate in enumerate(sorted_candidates, start=1):
        candidate["rank"] = rank_idx

    return sorted_candidates


def build_summary_dataframe(ranked_candidates: List[Dict[str, Any]]) -> pd.DataFrame:
    """
    Build a pandas DataFrame from ranked candidates for display/export.

    Args:
        ranked_candidates: Output from rank_candidates().

    Returns:
        A DataFrame with columns suitable for display in Streamlit.
    """
    rows = []
    for c in ranked_candidates:
        rows.append(
            {
                "Rank": c.get("rank", "-"),
                "Candidate": c.get("name", "Unknown"),
                "Match Score (%)": c.get("match_score", 0),
                "Semantic Score (%)": c.get("semantic_score", 0),
                "Skill Score (%)": c.get("skill_score", 0),
                "Experience": c.get("experience", "Not specified"),
                "Total Skills Found": len(c.get("skills", [])),
                "Matched Skills": len(c.get("matched_skills", [])),
                "Missing Skills": len(c.get("missing_skills", [])),
            }
        )
    return pd.DataFrame(rows)
