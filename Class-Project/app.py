"""
app.py
------
Main Streamlit dashboard for the Intelligent Resume Screening Platform.

Screens:
  1. Input  — Job description + PDF upload + Screen button
  2. Results — Ranked candidates with expandable detail cards
"""

import streamlit as st
import pandas as pd
import io

from parser import extract_text_from_pdf
from extractor import extract_all, extract_skills
from matcher import compute_final_score
from ranking import rank_candidates, build_summary_dataframe

# ---------------------------------------------------------------------------
# Page configuration  (must be first Streamlit call)
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="AI Resume Screener",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------------------------------------------------------------------------
# Custom CSS — premium dark glassmorphism theme
# ---------------------------------------------------------------------------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

    html, body, [class*="css"], .stApp {
        font-family: 'Inter', sans-serif !important;
        background-color: #0f0c29 !important;
    }
    .block-container { padding-top: 1.5rem !important; }

    /* ── Hero ── */
    .hero-wrap {
        text-align: center;
        padding: 2.2rem 1rem 1.6rem;
        background: linear-gradient(135deg, rgba(102,126,234,0.12) 0%, rgba(167,139,250,0.12) 100%);
        border-radius: 20px;
        border: 1px solid rgba(102,126,234,0.28);
        margin-bottom: 2.2rem;
    }
    .hero-wrap h1 {
        font-size: 2.6rem;
        font-weight: 800;
        background: linear-gradient(135deg, #667eea 0%, #a78bfa 55%, #f093fb 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin: 0 0 0.4rem;
    }
    .hero-wrap p {
        color: #94a3b8;
        font-size: 1.05rem;
        margin: 0;
    }

    /* ── Section label ── */
    .sec-label {
        font-size: 0.72rem;
        font-weight: 700;
        letter-spacing: 0.13em;
        text-transform: uppercase;
        color: #667eea;
        margin-bottom: 0.35rem;
    }

    /* ── Metric strip ── */
    .metrics-strip {
        display: flex;
        gap: 1rem;
        margin: 0 0 2rem;
        flex-wrap: wrap;
    }
    .m-card {
        flex: 1;
        min-width: 140px;
        background: rgba(255,255,255,0.04);
        border: 1px solid rgba(255,255,255,0.09);
        border-radius: 16px;
        padding: 1.1rem 1.3rem;
        text-align: center;
        transition: transform .2s, border-color .2s;
    }
    .m-card:hover { transform: translateY(-3px); border-color: rgba(102,126,234,.4); }
    .m-val {
        font-size: 1.9rem;
        font-weight: 800;
        background: linear-gradient(135deg,#667eea,#a78bfa);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    .m-lbl { font-size: .82rem; color: #94a3b8; margin-top: .15rem; }

    /* ── Candidate card ── */
    .c-card {
        background: rgba(255,255,255,0.03);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 18px;
        padding: 1.4rem 1.5rem 1rem;
        margin-bottom: 0.5rem;
        transition: border-color .2s, transform .2s;
    }
    .c-card:hover { border-color: rgba(102,126,234,.42); transform: translateY(-2px); }
    .c-hdr { display: flex; align-items: center; gap: .9rem; margin-bottom: .6rem; }
    .rank-badge {
        width: 42px; height: 42px; border-radius: 50%;
        display: flex; align-items: center; justify-content: center;
        font-weight: 800; font-size: 1rem; flex-shrink: 0;
    }
    .r1 { background: linear-gradient(135deg,#FFD700,#FFA500); color: #1a1a2e; }
    .r2 { background: linear-gradient(135deg,#C0C0C0,#A8A8A8); color: #1a1a2e; }
    .r3 { background: linear-gradient(135deg,#CD7F32,#A0522D); color: #fff; }
    .rn { background: rgba(255,255,255,.1); color: #94a3b8; }
    .c-name { font-size: 1.2rem; font-weight: 700; color: #e2e8f0; }
    .c-meta { font-size: .82rem; color: #94a3b8; margin-top: .12rem; }
    .s-pill {
        margin-left: auto; padding: .38rem .95rem;
        border-radius: 50px; font-weight: 700; font-size: .95rem;
    }
    .sh { background: rgba(34,197,94,.18); color: #4ade80; border: 1px solid rgba(34,197,94,.35); }
    .sm { background: rgba(234,179,8,.18);  color: #facc15; border: 1px solid rgba(234,179,8,.35); }
    .sl { background: rgba(239,68,68,.18);  color: #f87171; border: 1px solid rgba(239,68,68,.3); }

    /* ── Skill tags ── */
    .sk { display: inline-block; padding: .2rem .6rem; border-radius: 50px;
          font-size: .73rem; font-weight: 500; margin: .15rem; }
    .sk-g { background: rgba(34,197,94,.13); color: #4ade80; border: 1px solid rgba(34,197,94,.28); }
    .sk-r { background: rgba(239,68,68,.11); color: #f87171; border: 1px solid rgba(239,68,68,.25); }
    .sk-b { background: rgba(102,126,234,.14); color: #a5b4fc; border: 1px solid rgba(102,126,234,.28); }

    /* ── Streamlit widget overrides ── */
    .stTextArea textarea {
        background: rgba(255,255,255,0.05) !important;
        border: 1px solid rgba(102,126,234,.35) !important;
        border-radius: 12px !important;
        color: #e2e8f0 !important;
    }
    .stButton > button {
        background: linear-gradient(135deg,#667eea,#a78bfa) !important;
        color: #fff !important; font-weight: 700 !important;
        font-size: 1rem !important; padding: .7rem 2rem !important;
        border-radius: 50px !important; border: none !important;
        box-shadow: 0 4px 18px rgba(102,126,234,.4) !important;
        transition: all .2s !important; width: 100% !important;
    }
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 28px rgba(102,126,234,.6) !important;
    }
    .stDownloadButton > button {
        background: rgba(255,255,255,.06) !important;
        color: #a5b4fc !important;
        border: 1px solid rgba(102,126,234,.38) !important;
        border-radius: 50px !important;
    }
    div[data-testid="stProgress"] > div > div > div > div {
        background: linear-gradient(90deg,#667eea,#a78bfa) !important;
    }
    hr { border-color: rgba(255,255,255,.08) !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# Session state
# ---------------------------------------------------------------------------
if "results" not in st.session_state:
    st.session_state.results = None
if "jd_skills" not in st.session_state:
    st.session_state.jd_skills = []


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def score_pill_cls(s):
    return "sh" if s >= 70 else ("sm" if s >= 45 else "sl")

def rank_badge_cls(r):
    return {1: "r1", 2: "r2", 3: "r3"}.get(r, "rn")

def skill_tags(skills, cls):
    return "".join(f'<span class="sk {cls}">{s}</span>' for s in skills)

def process_resumes(files, jd_text):
    jd_skills = extract_skills(jd_text)
    candidates = []
    bar = st.progress(0, text="Starting analysis…")
    for i, f in enumerate(files):
        bar.progress((i + 1) / len(files), text=f"Processing {f.name} ({i+1}/{len(files)})…")
        raw = extract_text_from_pdf(f)
        if raw.startswith("[ERROR]"):
            st.warning(f"⚠️ Could not parse **{f.name}**: {raw}")
            continue
        info = extract_all(raw)
        scores = compute_final_score(
            resume_text=raw, jd_text=jd_text,
            resume_skills=info["skills"], jd_skills=jd_skills,
        )
        candidates.append({
            "filename": f.name,
            "name": info["name"],
            "skills": info["skills"],
            "experience": info["experience"],
            **scores,
        })
    bar.empty()
    return rank_candidates(candidates), jd_skills


# ---------------------------------------------------------------------------
# ── HERO HEADER ──
# ---------------------------------------------------------------------------
st.markdown("""
<div class="hero-wrap">
    <h1>🧠 AI Resume Screener</h1>
    <p>Intelligent candidate ranking powered by Semantic AI &amp; NLP — built for modern recruiters</p>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# ── SCREEN 1: INPUT ──
# ---------------------------------------------------------------------------
col_jd, col_up = st.columns([1, 1], gap="large")

with col_jd:
    st.markdown('<div class="sec-label">📋 Job Description</div>', unsafe_allow_html=True)
    jd_text = st.text_area(
        "jd_area",
        placeholder=(
            "Paste the full job description here…\n\n"
            "Example: We are looking for a Python Developer with 3+ years of experience "
            "in machine learning, FastAPI, Docker, PostgreSQL, and AWS…"
        ),
        height=260,
        label_visibility="collapsed",
    )

with col_up:
    st.markdown('<div class="sec-label">📄 Upload Resumes (PDF)</div>', unsafe_allow_html=True)
    uploaded_files = st.file_uploader(
        "resumes",
        type=["pdf"],
        accept_multiple_files=True,
        label_visibility="collapsed",
    )
    if uploaded_files:
        st.markdown(
            f"<p style='color:#94a3b8;font-size:.84rem;margin-top:.4rem'>"
            f"✅ {len(uploaded_files)} resume(s) ready to screen</p>",
            unsafe_allow_html=True,
        )

st.markdown("<div style='height:.8rem'></div>", unsafe_allow_html=True)
_, btn_col, _ = st.columns([1, 2, 1])
with btn_col:
    run = st.button("🚀  Screen Candidates", use_container_width=True)

st.markdown("<hr>", unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# Pipeline
# ---------------------------------------------------------------------------
if run:
    if not jd_text.strip():
        st.error("❗ Please enter a job description before screening.")
    elif not uploaded_files:
        st.error("❗ Please upload at least one PDF resume.")
    else:
        with st.spinner("Analysing resumes with AI…"):
            ranked, jd_skills = process_resumes(uploaded_files, jd_text.strip())
        st.session_state.results = ranked
        st.session_state.jd_skills = jd_skills

# ---------------------------------------------------------------------------
# ── SCREEN 2: RESULTS ──
# ---------------------------------------------------------------------------
if st.session_state.results:
    results = st.session_state.results
    jd_skills = st.session_state.jd_skills

    total = len(results)
    top_score = results[0]["match_score"] if results else 0
    avg_score = sum(c["match_score"] for c in results) / total if results else 0
    top_name  = results[0]["name"] if results else "—"

    # ── Metric strip ──
    st.markdown(f"""
    <div class="metrics-strip">
        <div class="m-card"><div class="m-val">{total}</div><div class="m-lbl">Candidates Analysed</div></div>
        <div class="m-card"><div class="m-val">{top_score:.1f}%</div><div class="m-lbl">Top Match Score</div></div>
        <div class="m-card"><div class="m-val">{avg_score:.1f}%</div><div class="m-lbl">Average Score</div></div>
        <div class="m-card"><div class="m-val" style="font-size:1.25rem">🏆</div>
            <div class="m-lbl">Top: <strong style="color:#e2e8f0">{top_name}</strong></div></div>
    </div>
    """, unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["📊 Ranked Results", "📋 Summary Table"])

    # ── Tab 1: Cards ──
    with tab1:
        st.markdown("<h3 style='color:#e2e8f0;font-weight:700;margin-bottom:1rem'>Candidate Rankings</h3>",
                    unsafe_allow_html=True)

        for c in results:
            rank  = c["rank"]
            score = c["match_score"]
            bc    = rank_badge_cls(rank)
            pc    = score_pill_cls(score)

            st.markdown(f"""
            <div class="c-card">
              <div class="c-hdr">
                <div class="rank-badge {bc}">#{rank}</div>
                <div>
                  <div class="c-name">{c['name']}</div>
                  <div class="c-meta">📁 {c['filename']} &nbsp;|&nbsp; 🕐 {c['experience']}</div>
                </div>
                <div class="s-pill {pc}">{score:.1f}%</div>
              </div>
            </div>
            """, unsafe_allow_html=True)

            sc1, sc2, sc3 = st.columns(3)
            with sc1:
                st.caption("🎯 Overall Match")
                st.progress(min(int(score), 100), text=f"{score:.1f}%")
            with sc2:
                st.caption("🔤 Semantic Similarity")
                st.progress(min(int(c["semantic_score"]), 100), text=f"{c['semantic_score']:.1f}%")
            with sc3:
                st.caption("🛠️ Skill Coverage")
                st.progress(min(int(c["skill_score"]), 100), text=f"{c['skill_score']:.1f}%")

            with st.expander(f"🔍 Full details — {c['name']}"):
                d1, d2 = st.columns(2)
                with d1:
                    st.markdown("**✅ Matched Skills**")
                    st.markdown(skill_tags(c["matched_skills"][:15], "sk-g") or "*None found*",
                                unsafe_allow_html=True)
                    st.markdown("<br>**🛠️ All Extracted Skills**", unsafe_allow_html=True)
                    st.markdown(skill_tags(c["skills"][:20], "sk-b") or "*None found*",
                                unsafe_allow_html=True)
                with d2:
                    st.markdown("**❌ Missing Skills (required by JD)**")
                    if c["missing_skills"]:
                        st.markdown(skill_tags(c["missing_skills"][:15], "sk-r"), unsafe_allow_html=True)
                    else:
                        st.success("All required skills present!")
                    st.markdown("<br>**🕐 Experience**", unsafe_allow_html=True)
                    st.info(c["experience"])

            st.markdown("<div style='height:.2rem'></div>", unsafe_allow_html=True)

    # ── Tab 2: Table ──
    with tab2:
        df = build_summary_dataframe(results)
        st.dataframe(
            df.style.background_gradient(subset=["Match Score (%)"], cmap="RdYlGn"),
            use_container_width=True,
            hide_index=True,
        )
        csv = io.StringIO()
        df.to_csv(csv, index=False)
        st.download_button(
            "⬇️ Download Results as CSV",
            data=csv.getvalue(),
            file_name="resume_screening_results.csv",
            mime="text/csv",
        )

    # JD skills detected
    if jd_skills:
        st.markdown("<hr>", unsafe_allow_html=True)
        with st.expander("📌 Skills detected in Job Description"):
            st.markdown(skill_tags(jd_skills, "sk-b"), unsafe_allow_html=True)
