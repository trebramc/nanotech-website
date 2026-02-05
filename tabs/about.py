import streamlit as st
import pandas as pd
from pathlib import Path

# -------------------------------------------------
# PAGE DATA
# -------------------------------------------------
@st.cache_data
def load_people():
    df = pd.read_excel("data/people.xlsx")
    df.columns = df.columns.str.strip().str.lower()
    return df

# -------------------------------------------------
# HELPERS
# -------------------------------------------------
def count_people(df, role=None, level=None, status=None):
    temp = df.copy()

    if role and "role" in temp.columns:
        temp = temp[temp["role"] == role]

    if level and "level" in temp.columns:
        temp = temp[temp["level"] == level]

    if status and "status" in temp.columns:
        temp = temp[temp["status"] == status]

    return len(temp)

# -------------------------------------------------
# RENDER TAB
# -------------------------------------------------
def render():
    df = load_people()

    # -------------------------------------------------
    # STYLES
    # -------------------------------------------------
    st.markdown("""
    <style>
    .hero {
        padding: 3rem 3rem;
        background: linear-gradient(135deg, #ff5f9e, #ff87b2, #ffc1d9);
        border-radius: 26px;
        color: white;
    }

    .hero h1 {
        font-size: 2.8rem;
        margin-bottom: 0.6rem;
    }

    .hero p {
        font-size: 1.1rem;
        max-width: 820px;
        opacity: 0.95;
    }

    .content-card {
        background: #ffffff;
        padding: 2.2rem;
        border-radius: 22px;
        box-shadow: 0 10px 26px rgba(0,0,0,0.08);
    }

    .section-hero {
        padding: 2rem;
        border-radius: 20px;
        background: linear-gradient(135deg, #ff9acb, #ffd1e6);
        box-shadow: 0 8px 22px rgba(0,0,0,0.08);
    }

    .stat {
        padding: 2.2rem;
        border-radius: 20px;
        background: linear-gradient(135deg, #ff7eb3, #ffb3d9);
        text-align: center;
        color: white;
        box-shadow: 0 10px 24px rgba(0,0,0,0.12);
    }

    .stat h1 {
        font-size: 3rem;
        margin-bottom: 0.3rem;
    }

    .stat p {
        margin: 0;
        font-weight: 500;
        font-size: 0.95rem;
    }
    </style>
    """, unsafe_allow_html=True)

    # -------------------------------------------------
    # HERO (TEXT ONLY — CLEAN)
    # -------------------------------------------------
    st.markdown("""
    <div class="hero">
        <h1>Nanotechnology Research Laboratory</h1>
        <p>
        A multidisciplinary research group advancing nanotechnology,
        materials science, and chemical engineering through rigorous
        experimentation, collaboration, and innovation.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    # -------------------------------------------------
    # MISSION & VISION
    # -------------------------------------------------
    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("""
        <div class="section-hero">
            <h3>Mission</h3>
            <p>
            To conduct high-impact research in nanotechnology and materials science,
            train students through hands-on scientific inquiry, and develop
            knowledge-driven solutions that address national and global challenges.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="section-hero">
            <h3>Vision</h3>
            <p>
            To be a leading academic research laboratory recognized for excellence
            in nanotechnology research, interdisciplinary collaboration, and the
            formation of future scientists and engineers.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    # -------------------------------------------------
    # ABOUT THE LAB (IMAGE + TEXT — YOUR REQUEST)
    # -------------------------------------------------
    col_img, col_txt = st.columns([1, 2], gap="large")

    with col_img:
        img_path = Path("assets/logos/lab_logo.png")
        if img_path.exists():
            st.image(img_path, use_container_width=True)


    with col_txt:
        st.markdown("""
        <div class="content-card">
            <h3>About the Laboratory</h3>
            <p>
            The Nanotechnology Research Laboratory focuses on the synthesis,
            characterization, and application of nanoscale materials. The group
            supports undergraduate, graduate, and faculty-led research across
            chemical engineering, materials science, and related disciplines.
            </p>
            <p>
            Through mentorship and collaborative research, the laboratory has trained
            students who pursue careers in academia, industry, and public service,
            while contributing to the advancement of nanoscience and engineering.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    # -------------------------------------------------
    # THROUGH THE YEARS
    # -------------------------------------------------
    st.subheader("Through the Years")

    c1, c2, c3, c4 = st.columns(4, gap="large")

    with c1:
        st.markdown(f"""
        <div class="stat">
            <h1>{count_people(df, role="Student", level="MS", status="Graduated")}</h1>
            <p>Graduated MS Students</p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
        <div class="stat">
            <h1>{count_people(df, role="Student", level="Undergraduate", status="Graduated")}</h1>
            <p>Graduated Undergraduates</p>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown(f"""
        <div class="stat">
            <h1>{count_people(df, role="Student", level="Undergraduate", status="Current")}</h1>
            <p>Current Undergraduates</p>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown(f"""
        <div class="stat">
            <h1>{count_people(df, role="Faculty", status="Current")}</h1>
            <p>Current Faculty</p>
        </div>
        """, unsafe_allow_html=True)
