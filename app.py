import streamlit as st

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="Nanotechnology Research Laboratory",
    layout="wide",
)


# -------------------------------------------------
# IMPORT TAB MODULES
# -------------------------------------------------
from tabs.about import render as about_tab
from tabs.people import render as people_tab
from tabs.publications import render as publications_tab
from tabs.contact import render as contact_tab
from tabs.tools import render as tools_tab
from tabs.research import render as research_tab
from tabs.active_research import render as active_projects_tab

# -------------------------------------------------
# SIDEBAR — AFFILIATIONS
# -------------------------------------------------
with st.sidebar:


    # ---- LOGOS IN ONE ROW ----
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("assets/logos/upd_logo.png", width=55)

    with col2:
        st.image("assets/logos/institution_logo.png", width=55)

    with col3:
        st.image("assets/logos/lab_logo.png", width=55)

    st.markdown(
        """
        <div style="
            margin-top: 12px;
            font-size: 12px;
            color: #777;
            line-height: 1.4;
        ">
            Official academic and institutional affiliations
        </div>
        """,
        unsafe_allow_html=True
    )

# -------------------------------------------------
# MAIN HEADER
# -------------------------------------------------

st.markdown(
    """
    <div style="margin-bottom: 0.5rem;">
        <h2 style="margin-bottom: 0.2rem;">
            Nanotechnology Research Laboratory
        </h2>
        <p style="
            margin: 0;
            color: #6b7280;
            font-size: 0.95rem;
            max-width: 720px;
        ">
            Department of Chemical Engineering | UP Diliman
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# -------------------------------------------------
# TABS
# -------------------------------------------------
tabs = st.tabs([
    "Home",
    "Research Areas",
    "Publications",
    "Active Projects",
    "People",
    "Tools",
    "Contact",
])

# -------------------------------------------------
# TAB CONTENT
# -------------------------------------------------
with tabs[0]:
    about_tab()

with tabs[4]:
    people_tab()

with tabs[2]:
    publications_tab()

with tabs[6]:
    contact_tab()

with tabs[5]:
    tools_tab()

with tabs[1]:
    research_tab()

with tabs[3]:
    active_projects_tab()
