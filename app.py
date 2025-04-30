import streamlit as st
from utils.manim_utils import generate_and_render_manim_video

st.set_page_config(
    page_title="Al-Khwarizmi",
    page_icon="🧮",
    layout="centered",
    initial_sidebar_state="auto",
)

st.markdown(
    """
    <style>
    .main {
        background: linear-gradient(135deg, #f8fafc 0%, #e0e7ef 100%);
    }
    .stButton>button {
        background: linear-gradient(90deg, #4f8cff 0%, #38e8ff 100%);
        color: white;
        border-radius: 8px;
        font-size: 1.1em;
        font-weight: bold;
        padding: 0.5em 2em;
        margin-top: 1em;
        box-shadow: 0 2px 8px #b6d0ff55;
        transition: 0.2s;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #38e8ff 0%, #4f8cff 100%);
        color: #222;
    }
    .big-title {
        font-size: 2.5em;
        font-weight: bold;
        color: #2d3a4a;
        text-align: center;
        margin-bottom: 0.2em;
    }
    .subtitle {
        font-size: 1.2em;
        color: #4f8cff;
        text-align: center;
        margin-bottom: 1.5em;
    }
    .footer {
        color: #888;
        font-size: 0.9em;
        text-align: center;
        margin-top: 2em;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="big-title">Al-Khwarizmi</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Turn your math ideas into beautiful animations instantly!<br>Powered by Google Gemini & ManimGL</div>',
    unsafe_allow_html=True,
)

with st.expander("ℹ️ How does it work?", expanded=False):
    st.markdown(
        """
        1. Enter a math concept in plain English (e.g. *Visualize the Riemann sum*).
        2. Click **Generate Animation**.
        3. The app will generate ManimGL code using Gemini and show the animation in a new window.
        """
    )

st.markdown("### Enter your math concept:")

concept = st.text_area(
    "",
    placeholder="e.g. Visualize the Riemann sum, Show the parabola y = x^2, Explain the concept of a derivative...",
    height=80,
)

col1, col2 = st.columns([1, 2])
with col2:
    if st.button("✨ Generate Animation"):
        if not concept.strip():
            st.warning("Please enter a math concept to visualize.")
        else:
            with st.spinner("Generating animation... Please wait."):
                result = generate_and_render_manim_video(concept, save_video=False)
            st.success("If ManimGL is installed correctly, a window should pop up with your animation!")
            st.info("If you don't see anything, check your ManimGL installation or try a simpler concept.")

st.markdown(
    """
    <div class="footer">
        Made with ❤️ using <a href="https://github.com/3b1b/manim" target="_blank">ManimGL</a> & <a href="https://ai.google.dev/" target="_blank">Google Gemini</a>.<br>
        <a href="https://github.com/ahmed88lk/math_Forevryone.git" target="_blank">GitHub Repo</a>
    </div>
    """,
    unsafe_allow_html=True,
)