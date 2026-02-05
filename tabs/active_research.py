import streamlit as st
import pandas as pd

# -------------------------------------------------
# LOAD DATA
# -------------------------------------------------
@st.cache_data
def load_active_research():
    df = pd.read_excel("data/active_research.xlsx")
    df.columns = df.columns.str.strip().str.lower()
    return df

# -------------------------------------------------
# HELPERS
# -------------------------------------------------
def clean_text(value):
    return "" if pd.isna(value) else str(value).strip()

# -------------------------------------------------
# RENDER TAB
# -------------------------------------------------
def render():

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
            <h1 style="margin-bottom: 12px;">Active Research</h1>
            <p style="font-size: 16px; max-width: 760px;">
                Ongoing and in-progress research projects currently being
                pursued by the Nanotechnology Research Laboratory.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # -------------------------------------------------
    # STYLES (MATCH PUBLICATIONS)
    # -------------------------------------------------
    st.markdown(
        """
        <style>
        .ar-card {
            background: #fff5fa;
            padding: 18px;
            border-radius: 16px;
            margin-bottom: 18px;
            box-shadow: 0 6px 18px rgba(255, 95, 158, 0.10);
        }

        .ar-card-featured {
            background: #fff0f6;
            padding: 18px;
            border-radius: 16px;
            margin-bottom: 18px;
            box-shadow: 0 10px 26px rgba(255, 95, 158, 0.20);
        }

        .ar-title {
            font-size: 18px;
            font-weight: 600;
            color: #2b2b2b;
            margin-bottom: 4px;
        }

        .ar-meta {
            font-size: 14px;
            color: #555;
            margin-bottom: 2px;
        }

        .ar-status {
            font-size: 13px;
            color: #777;
            margin-bottom: 6px;
        }

        .ar-tag {
            background: rgba(255, 95, 158, 0.18);
            color: #b4004e;
            padding: 4px 10px;
            border-radius: 999px;
            font-size: 12px;
            margin-right: 6px;
            display: inline-block;
            margin-top: 6px;
        }

        .ar-featured-badge {
            background: linear-gradient(135deg, #ff6aa6, #ff8fbf);
            color: white;
            font-size: 11px;
            font-weight: 600;
            padding: 4px 10px;
            border-radius: 999px;
            display: inline-block;
            margin-bottom: 6px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # -------------------------------------------------
    # LOAD & PARSE DATA
    # -------------------------------------------------
    df = load_active_research()

    projects = []
    all_tags = set()

    for _, row in df.iterrows():
        tags = (
            [t.strip() for t in str(row.get("keywords")).split(";")]
            if pd.notna(row.get("keywords"))
            else []
        )

        all_tags.update(tags)

        projects.append({
            "id": clean_text(row.get("id")),
            "year": int(row.get("year")),
            "title": clean_text(row.get("title")),
            "researchers": clean_text(row.get("researchers")),
            "status": clean_text(row.get("status")),
            "tags": sorted(tags),
            "description": clean_text(row.get("description")),
            "link": clean_text(row.get("link")),
            "contact": clean_text(row.get("contact")),
            "featured": bool(row.get("featured", False)),
        })

    projects.sort(key=lambda x: x["year"], reverse=True)

    # -------------------------------------------------
    # FILTERS
    # -------------------------------------------------
    col1, col2 = st.columns([2, 3])

    with col1:
        tag_filter = st.multiselect(
            "Filter by keywords",
            sorted(all_tags),
            key="active_tag_filter"
        )

    with col2:
        search_query = st.text_input(
            "Search active research",
            placeholder="Title, researcher, keyword, status…",
            key="active_search"
        )

    if tag_filter:
        projects = [
            p for p in projects
            if any(t in p["tags"] for t in tag_filter)
        ]

    if search_query:
        q = search_query.lower()
        projects = [
            p for p in projects
            if q in p["title"].lower()
            or q in p["researchers"].lower()
            or q in p["description"].lower()
            or q in p["status"].lower()
            or any(q in t.lower() for t in p["tags"])
        ]

    # -------------------------------------------------
    # GROUP BY YEAR
    # -------------------------------------------------
    years = sorted({p["year"] for p in projects}, reverse=True)

    for year in years:
        year_projects = [p for p in projects if p["year"] == year]
        if not year_projects:
            continue

        st.markdown(f"## {year}")

        for p in year_projects:

            card_class = "ar-card-featured" if p["featured"] else "ar-card"
            st.markdown(f"<div class='{card_class}'>", unsafe_allow_html=True)

            if p["featured"]:
                st.markdown(
                    "<div class='ar-featured-badge'>FEATURED PROJECT</div>",
                    unsafe_allow_html=True
                )

            # TITLE
            st.markdown(
                f"<div class='ar-title'>{p['title']}</div>",
                unsafe_allow_html=True
            )

            # RESEARCHERS
            if p["researchers"]:
                st.markdown(
                    f"<div class='ar-meta'>{p['researchers']}</div>",
                    unsafe_allow_html=True
                )

            # STATUS
            if p["status"]:
                st.markdown(
                    f"<div class='ar-status'>Status: {p['status']}</div>",
                    unsafe_allow_html=True
                )

            # TAGS
            if p["tags"]:
                st.markdown(
                    "".join(f"<span class='ar-tag'>{t}</span>" for t in p["tags"]),
                    unsafe_allow_html=True
                )

            # DETAILS
            with st.expander("Project details"):
                if p["description"]:
                    st.markdown("**Description**")
                    st.write(p["description"])

                if p["link"]:
                    st.markdown(f"[Project link →]({p['link']})")

                if p["contact"]:
                    st.markdown("**Contact**")
                    st.write(p["contact"])

            st.markdown("</div>", unsafe_allow_html=True)
