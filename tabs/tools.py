import streamlit as st

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
            <h1 style="margin-bottom: 12px;">Tools</h1>
            <p style="font-size: 16px; max-width: 720px;">
                Computational tools and digital resources developed by the
                Nanotechnology Research Laboratory. This section will expand
                as tools are released.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # -------------------------------------------------
    # DEVELOPMENT NOTICE
    # -------------------------------------------------
    st.markdown(
        """
        <div style="
            background: #fff0f6;
            padding: 18px 22px;
            border-radius: 16px;
            margin-bottom: 44px;
            border-left: 6px solid #ff5f9e;
            font-weight: 500;
        ">
            Tools are currently under development.<br>
            Previews shown below.
        </div>
        """,
        unsafe_allow_html=True
    )

    # -------------------------------------------------
    # TOOL DATA
    # -------------------------------------------------
    tools = [
        {
            "name": "Particle Size Analysis Tool",
            "description": (
                "Analyzes particle size distributions from experimental or "
                "image-based data. Generates PSD plots, D10/D50/D90 metrics, "
                "and summary statistics."
            ),
            "status": "Work in progress",
            "access": "Free (planned)",
        },
        {
            "name": "Crystallization Imaging Tool",
            "description": (
                "Processes optical or microscopic images of crystallization "
                "experiments. Supports nucleation tracking, growth visualization, "
                "and basic image analysis."
            ),
            "status": "Work in progress",
            "access": "Academic use",
        },
        {
            "name": "Crystallization Kinetics Simulator",
            "description": (
                "Simulates crystallization kinetics under cooling or antisolvent "
                "conditions, including supersaturation profiles, nucleation, "
                "and crystal growth rates."
            ),
            "status": "Work in progress",
            "access": "Academic use",
        },
    ]

    # -------------------------------------------------
    # TOOL GRID
    # -------------------------------------------------
    cols = st.columns(3, gap="large")

    for i, tool in enumerate(tools):
        with cols[i % 3]:

            # ---- GRADIENT TITLE (SAME AS PEOPLE TAB) ----
            st.markdown(
                f"""
                <div style="
                    background: linear-gradient(135deg, #ff5f9e, #ff87b2);
                    padding: 20px 22px;
                    border-radius: 22px;
                    margin-bottom: 16px;
                    color: white;
                    font-weight: 600;
                    font-size: 22px;
                    line-height: 1.25;
                ">
                    {tool['name']}
                </div>
                """,
                unsafe_allow_html=True
            )

            # ---- DESCRIPTION ----
            st.write(tool["description"])

            st.markdown("<div style='height:18px'></div>", unsafe_allow_html=True)

            # ---- STATUS / ACCESS ----
            col_a, col_b = st.columns(2)

            with col_a:
                st.caption("Status")
                st.markdown(
                    """
                    <div style="
                        background: #eaf8ec;
                        padding: 8px 12px;
                        border-radius: 10px;
                        font-size: 14px;
                        text-align: center;
                        color: #1b7f3b;
                        font-weight: 500;
                    ">
                        Work in progress
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            with col_b:
                st.caption("Access")
                st.markdown(
                    f"""
                    <div style="
                        background: #eef4ff;
                        padding: 8px 12px;
                        border-radius: 10px;
                        font-size: 14px;
                        text-align: center;
                        color: #1d4ed8;
                        font-weight: 500;
                    ">
                        {tool['access']}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            st.markdown(
                "<div style='margin-top:16px; font-size:13px; color:#777;'>"
                "More details coming soon</div>",
                unsafe_allow_html=True
            )

    # -------------------------------------------------
    # FOOTER / CTA
    # -------------------------------------------------
    st.markdown(
        """
        <div style="
            margin-top: 56px;
            padding: 28px 32px;
            border-radius: 20px;
            background: #fff7fb;
            border: 1px dashed #ffb6d2;
        ">
            <strong>Interested in early access or collaboration?</strong><br><br>
            Reach out through the <strong>Contact Us</strong> page to:
            <ul style="margin-top: 10px;">
                <li>request beta access</li>
                <li>collaborate on tool development</li>
                <li>deploy tools for academic or industrial use</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )
