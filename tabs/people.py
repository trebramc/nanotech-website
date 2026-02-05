import streamlit as st
import pandas as pd
import os
from pathlib import Path

# -------------------------------------------------
# LOAD DATA
# -------------------------------------------------
@st.cache_data
def load_people():
    df = pd.read_excel("data/people.xlsx")
    df.columns = df.columns.str.strip().str.lower()
    return df

# -------------------------------------------------
# HELPERS
# -------------------------------------------------
def clean_text(value):
    return "" if pd.isna(value) else str(value).strip()

def resolve_image(image_value):
    if pd.isna(image_value) or not image_value:
        return "assets/people/placeholder.png"

    base = os.path.splitext(str(image_value))[0]
    for ext in [".png", ".jpg", ".jpeg"]:
        path = f"assets/people/{base}{ext}"
        if os.path.exists(path):
            return path

    return "assets/people/placeholder.png"

def subtitle_text(p):
    if p["status"] == "Graduated":
        return "Alumni"
    if p["role"] == "Student":
        return f"{p['level']} · {p['status']}".strip(" ·")
    return p["role"]

def normalize_link(url):
    """Ensure links are clickable even if http(s) is missing"""
    if not url:
        return ""
    if url.startswith("http://") or url.startswith("https://"):
        return url
    return f"https://{url}"

# -------------------------------------------------
# RENDER TAB
# -------------------------------------------------
def render():
    df = load_people()

    # -------------------------------------------------
    # HERO SECTION
    # -------------------------------------------------
    st.markdown(
        """
        <div style="
            background: linear-gradient(135deg, #ff5f9e, #ff87b2, #ffc1d9);
            padding: 48px 40px;
            border-radius: 24px;
            margin-bottom: 40px;
            color: white;
        ">
            <h1 style="margin-bottom: 12px;">People</h1>
            <p style="font-size: 16px; max-width: 760px;">
                Get to know the people behind the Nanotechnology Research Laboratory —
                faculty, researchers, and students working across crystallization,
                sustainable processes, and materials science.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # -------------------------------------------------
    # STYLES
    # -------------------------------------------------
    st.markdown("""
    <style>
    .name-box {
        background: linear-gradient(135deg, #ff5f9e, #ff87b2, #ffc1d9);
        border-radius: 16px;
        padding: 12px 14px;
        text-align: center;
        box-shadow: 0 8px 20px rgba(255, 95, 158, 0.35);
        cursor: pointer;
    }

    .name-box-name {
        color: white;
        font-weight: 700;
        font-size: 1rem;
        line-height: 1.2;
    }

    .name-box-role {
        color: rgba(255,255,255,0.85);
        font-size: 0.85rem;
        margin-top: 4px;
    }

    .popover-name {
        background: linear-gradient(135deg, #ff5f9e, #ff87b2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 700;
    }
    </style>
    """, unsafe_allow_html=True)

    # -------------------------------------------------
    # PARSE PEOPLE
    # -------------------------------------------------
    people = []
    for _, row in df.iterrows():
        people.append({
            "name": clean_text(row.get("name")),
            "role": clean_text(row.get("role")),
            "level": clean_text(row.get("level")),
            "status": clean_text(row.get("status")),
            "image": resolve_image(row.get("image")),
            "bio": clean_text(row.get("bio")),
            "research": (
                [r.strip() for r in str(row.get("research")).split(";")]
                if pd.notna(row.get("research"))
                else []
            ),
            "link": clean_text(row.get("link")),
        })

    # -------------------------------------------------
    # GROUP DEFINITIONS
    # -------------------------------------------------
    groups = [
        ("Faculty", lambda p: p["role"] == "Faculty" and p["status"] == "Current"),
        ("Graduate Students", lambda p: p["role"] == "Student" and p["level"] in ["MS", "PhD"] and p["status"] == "Current"),
        ("Undergraduate Students", lambda p: p["role"] == "Student" and p["level"] == "Undergraduate" and p["status"] == "Current"),
        ("Alumni", lambda p: p["status"] == "Graduated"),
    ]

    # -------------------------------------------------
    # RENDER GROUPS
    # -------------------------------------------------
    for section_title, rule in groups:
        section_people = [p for p in people if rule(p)]
        if not section_people:
            continue

        st.markdown(f"### {section_title}")
        cols = st.columns(4)

        for i, p in enumerate(section_people):
            with cols[i % 4]:

                st.image(p["image"], use_container_width=True)
                st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

                # ---- NAME BOX ----
                st.markdown(
                    f"""
                    <div class="name-box">
                        <div class="name-box-name">{p['name']}</div>
                        <div class="name-box-role">{subtitle_text(p)}</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                # ---- POPOVER ----
                with st.popover("View details", use_container_width=True):

                    st.markdown(
                        f"<h3 class='popover-name'>{p['name']}</h3>",
                        unsafe_allow_html=True
                    )

                    st.caption(subtitle_text(p))

                    if p["bio"]:
                        st.write(p["bio"])

                    if p["research"]:
                        st.markdown("**Research Interests**")
                        for r in p["research"]:
                            st.markdown(f"- {r}")

                    if p["link"]:
                        st.markdown("**Profile / Website**")
                        url = normalize_link(p["link"])
                        st.markdown(f"- 🔗 [Visit profile]({url})")

