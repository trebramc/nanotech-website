import streamlit as st
from pathlib import Path
import pandas as pd


# -------------------------------------------------
# RENDER TAB
# -------------------------------------------------
def render():

    # -------------------------------------------------
    # HERO SECTION (CONSISTENT WITH OTHER TABS)
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
            <h1 style="margin-bottom: 12px;">Research Areas</h1>
            <p style="font-size: 16px; max-width: 760px;">
                Our laboratory focuses on fundamental and applied research in
                crystallization, sustainable recovery processes, and bioactive
                compound extraction.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # -------------------------------------------------
    # LOAD DATA
    # -------------------------------------------------
    data_path = Path("data/research_tracks.xlsx")

    if not data_path.exists():
        st.error("Research data file not found.")
        return

    df = pd.read_excel(data_path)

    # -------------------------------------------------
    # GRID
    # -------------------------------------------------
    cols = st.columns(3, gap="large")

    for i, (_, row) in enumerate(df.iterrows()):
        with cols[i % 3]:

            # ---- IMAGE ----
            img_path = Path(row["image_path"])
            if img_path.exists():
                st.image(img_path, use_container_width=True)
            else:
                st.image(
                    "assets/placeholders/square_placeholder.png",
                    use_container_width=True
                )

            # ---- PINK TITLE PILL (MATCHES PEOPLE CARDS) ----
            st.markdown(
                f"""
                <div style="
                    background: linear-gradient(135deg, #ff6aa6, #ff8fbf);
                    padding: 14px 18px;
                    border-radius: 18px;
                    margin-top: 12px;
                    margin-bottom: 10px;
                    text-align: center;
                    color: white;
                    font-weight: 600;
                    font-size: 18px;
                    box-shadow: 0 6px 16px rgba(255, 95, 158, 0.25);
                ">
                    {row["title"]}
                </div>
                """,
                unsafe_allow_html=True
            )

            # ---- LEARN MORE DROPDOWN ----
            with st.expander("Learn more"):
                st.write(row["description"])
