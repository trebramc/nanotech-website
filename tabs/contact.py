import streamlit as st
import urllib.parse

# -------------------------------------------------
# RENDER TAB
# -------------------------------------------------
def render():

    # -------------------------------------------------
    # HERO SECTION (PINK)
    # -------------------------------------------------
    st.markdown(
        """
        <div style="
            background: linear-gradient(135deg, #ff5f9e, #ff87b2, #ffc1d9);
            padding: 48px 40px;
            border-radius: 24px;
            margin-bottom: 36px;
            color: white;
        ">
            <h1 style="margin-bottom: 12px;">Contact Us</h1>
            <p style="font-size: 16px; max-width: 720px;">
                For inquiries, collaborations, or student opportunities, please reach out
                using the form below or through our official laboratory channels.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    col_info, col_form = st.columns([2, 3], gap="large")

    # -------------------------------------------------
    # LABORATORY CONTACT (LEFT)
    # -------------------------------------------------
    with col_info:

        st.markdown(
            """
            <div style="
                background-color: #fff5fa;
                padding: 28px;
                border-radius: 18px;
                box-shadow: 0 6px 18px rgba(255, 95, 158, 0.12);
            ">
            """,
            unsafe_allow_html=True
        )

        st.markdown("### Laboratory Contact")

        st.markdown(
            """
            **Nanotechnology Research Laboratory**  
            University of the Philippines Diliman  
            Department of Chemical Engineering
            """
        )

        st.markdown("<div style='height:18px'></div>", unsafe_allow_html=True)

        # ---- EMAIL BOX ----
        st.markdown(
            """
            <div style="
                background: #ffe1ef;
                padding: 14px 16px;
                border-radius: 14px;
                margin-bottom: 14px;
            ">
                <strong>Email</strong><br>
                <a href="mailto:icdelacruz1@up.edu.ph">icdelacruz1@up.edu.ph</a>
            </div>
            """,
            unsafe_allow_html=True
        )

        # ---- SOCIAL MEDIA BOX ----
        st.markdown(
            """
            <div style="
                background: #ffe1ef;
                padding: 14px 16px;
                border-radius: 14px;
                margin-bottom: 14px;
            ">
                <strong>Social Media</strong><br>
                <a href="https://facebook.com" target="_blank">Facebook</a><br>
                <a href="https://instagram.com" target="_blank">Instagram</a>
            </div>
            """,
            unsafe_allow_html=True
        )

        # ---- ADDRESS BOX ----
        st.markdown(
            """
            <div style="
                background: #ffe1ef;
                padding: 14px 16px;
                border-radius: 14px;
            ">
                <strong>Address</strong><br>
                DChE Building, Room C205<br>
                University of the Philippines Diliman Campus
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("</div>", unsafe_allow_html=True)

    # -------------------------------------------------
    # CONTACT FORM (RIGHT)
    # -------------------------------------------------
    with col_form:

        st.markdown(
            """
            <div style="
                background: #fff0f6;
                padding: 28px;
                border-radius: 18px;
                box-shadow: 0 8px 22px rgba(255, 95, 158, 0.16);
            ">
            """,
            unsafe_allow_html=True
        )

        st.markdown("### Send us a Message!")
        st.caption("We typically respond within 2–3 working days.")

        subject_options = [
            "Research collaboration",
            "Student opportunities",
            "Publication inquiry",
            "Laboratory visit",
            "Please specify",
        ]

        subject_choice = st.selectbox(
            "Subject",
            subject_options,
            key="subject_select"
        )

        custom_subject = ""
        if subject_choice == "Please specify":
            custom_subject = st.text_input(
                "Custom subject",
                placeholder="Enter your subject here",
                key="custom_subject"
            )

        with st.form("contact_form"):
            name = st.text_input("Name")
            email = st.text_input("Email")
            message = st.text_area("Message", height=140)

            submitted = st.form_submit_button("Send Message")

        if submitted:
            final_subject = custom_subject if subject_choice == "Please specify" else subject_choice

            if not name or not email or not message or not final_subject:
                st.warning("Please fill in all fields before sending.")
            else:
                full_subject = f"{final_subject} — Inquiry from {name}"
                body = f"From: {name} ({email})\n\n{message}"

                mailto_link = (
                    "mailto:icdelacruz1@up.edu.ph?"
                    + urllib.parse.urlencode(
                        {
                            "subject": full_subject,
                            "body": body,
                        },
                        quote_via=urllib.parse.quote
                    )
                )

                st.success("Your email is ready to be sent.")
                st.markdown(f"[Click here to send your message →]({mailto_link})")

        st.markdown("</div>", unsafe_allow_html=True)
