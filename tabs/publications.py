import streamlit as st
import pandas as pd
import os

# -------------------------------------------------
# LOAD DATA
# -------------------------------------------------
@st.cache_data
def load_publications():
    df = pd.read_excel("data/publications.xlsx")
    df.columns = df.columns.str.strip().str.lower()
    return df

# -------------------------------------------------
# HELPERS
# -------------------------------------------------
def clean_text(value):
    return "" if pd.isna(value) else str(value).strip()

def resolve_image(image_value):
    if pd.isna(image_value):
        return "assets/publications/placeholder.png"

    base = os.path.splitext(str(image_value))[0]
    for ext in [".png", ".jpg", ".jpeg"]:
        path = f"assets/publications/{base}{ext}"
        if os.path.exists(path):
            return path

    return "assets/publications/placeholder.png"

# -------------------------------------------------
# RENDER TAB
# -------------------------------------------------
def render():

    pubs_df = load_publications()

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
            <h1 style="margin-bottom: 12px;">Publications</h1>
            <p style="font-size: 16px; max-width: 760px;">
                Peer-reviewed journal articles, conference papers, and scholarly
                outputs produced by the Nanotechnology Research Laboratory.
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
    .pub-card {
        background: #fff5fa;
        padding: 18px;
        border-radius: 16px;
        margin-bottom: 18px;
        box-shadow: 0 6px 18px rgba(255, 95, 158, 0.10);
    }

    .pub-title-row {
        display: flex;
        align-items: center;
        gap: 10px;
        flex-wrap: wrap;
        margin-bottom: 2px;
    }

    .pub-title {
        font-size: 18px;
        font-weight: 600;
        color: #2b2b2b;
    }

    .featured-tag {
        background: rgba(255, 95, 158, 0.18);
        color: #b4004e;
        padding: 3px 10px;
        border-radius: 999px;
        font-size: 12px;
        font-weight: 600;
    }

    .pub-authors {
        font-size: 14px;
        color: #555;
        margin-bottom: 2px;
    }

    .pub-journal {
        font-size: 13px;
        color: #777;
        margin-bottom: 6px;
    }

    .pub-tag {
        background: rgba(255, 95, 158, 0.18);
        color: #b4004e;
        padding: 4px 10px;
        border-radius: 999px;
        font-size: 12px;
        margin-right: 6px;
        display: inline-block;
        margin-top: 6px;
    }
    </style>
    """, unsafe_allow_html=True)

    # -------------------------------------------------
    # PARSE PUBLICATIONS
    # -------------------------------------------------
    publications = []
    all_tags = set()

    for _, row in pubs_df.iterrows():
        tags = (
            [t.strip() for t in str(row.get("keywords")).split(";")]
            if pd.notna(row.get("keywords"))
            else []
        )

        all_tags.update(tags)

        publications.append({
            "id": clean_text(row.get("id")),
            "year": int(row.get("year")),
            "title": clean_text(row.get("title")),
            "authors": clean_text(row.get("authors")),
            "tags": sorted(tags),
            "abstract": clean_text(row.get("abstract")),
            "image": resolve_image(row.get("image")),
            "link": clean_text(row.get("link")),
            "contact": clean_text(row.get("contact")),
            "journal": clean_text(row.get("journal")),
            "featured": bool(row.get("featured", False)),
        })

    publications.sort(key=lambda x: x["year"], reverse=True)

    # -------------------------------------------------
    # FILTERS
    # -------------------------------------------------
    col1, col2 = st.columns([2, 3])

    with col1:
        tag_filter = st.multiselect(
            "Filter by keywords",
            sorted(all_tags),
            key="pub_tag_filter"
        )

    with col2:
        search_query = st.text_input(
            "Search publications",
            placeholder="Title, author, keyword, journal…",
            key="pub_search"
        )

    if tag_filter:
        publications = [
            p for p in publications
            if any(t in p["tags"] for t in tag_filter)
        ]

    if search_query:
        q = search_query.lower()
        publications = [
            p for p in publications
            if q in p["title"].lower()
            or q in p["authors"].lower()
            or q in p["abstract"].lower()
            or q in p["journal"].lower()
            or any(q in t.lower() for t in p["tags"])
        ]

    # -------------------------------------------------
    # GROUP BY YEAR
    # -------------------------------------------------
    years = sorted({p["year"] for p in publications}, reverse=True)

    for year in years:
        year_pubs = [p for p in publications if p["year"] == year]
        if not year_pubs:
            continue

        st.markdown(f"## {year}")

        for p in year_pubs:

            st.markdown("<div class='pub-card'>", unsafe_allow_html=True)

            col_img, col_txt = st.columns([1, 4])

            with col_img:
                st.image(p["image"], use_container_width=True)

            with col_txt:
                st.markdown(
                    f"""
                    <div class="pub-title-row">
                        <div class="pub-title">{p['title']}</div>
                        {("<div class='featured-tag'>Featured</div>" if p["featured"] else "")}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                if p["authors"]:
                    st.markdown(f"<div class='pub-authors'>{p['authors']}</div>", unsafe_allow_html=True)

                if p["journal"]:
                    st.markdown(f"<div class='pub-journal'>{p['journal']}</div>", unsafe_allow_html=True)

                if p["tags"]:
                    st.markdown(
                        "".join(f"<span class='pub-tag'>{t}</span>" for t in p["tags"]),
                        unsafe_allow_html=True
                    )

                with st.expander("Abstract & links"):
                    if p["abstract"]:
                        st.markdown("**Abstract**")
                        st.write(p["abstract"])

                    if p["link"]:
                        st.markdown(f"[Read full paper →]({p['link']})")

                    if p["contact"]:
                        st.markdown("**Contact**")
                        st.write(p["contact"])

            st.markdown("</div>", unsafe_allow_html=True)
