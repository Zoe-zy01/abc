import streamlit as st
from PIL import Image
import os

def home_page():
    left_col, right_col = st.columns(2)
    left_col.markdown(
        """
        <h4>Ziyi Zoe Wang</h4>
        <p>Recent Master's Graduate in Marketing<br>
        Chinese University of Hong Kong<br>
        12 Chak Cheung St., Ma Liu Shui, HKSAR<br>
        <a href="mailto:ziyi.wang1@outlook.com">ziyi.wang1@outlook.com</a></p>
        """,
        unsafe_allow_html=True
    )

    # add a photo to the right column
    image_path = os.path.join("static", "images", "image.jpg")
    if os.path.exists(image_path):
        image = Image.open(image_path)
        right_col.image(image, width=200)
    else:
        right_col.warning("Profile image not found")

    st.markdown("---")

    st.markdown(
        """
        ### About Me
        I am a recent master's graduate in Marketing from the Chinese University of Hong Kong, eager to apply my knowledge and skills in a professional setting. During my academic journey, I developed a strong foundation in market strategy, machine learning, and data visualization.

        As part of my master's program, I completed several projects that involved working with real-world cases and applying various marketing strategies and data techniques. These projects allowed me to gain hands-on experience in digital marketing, data preprocessing and exploratory data analysis.

        I am passionate about leveraging data to drive insights and make informed decisions. I am a quick learner, a collaborative team player, and possess strong problem-solving skills. I am excited to contribute my skills and grow as a marketing professional in a dynamic and challenging environment.
        """
    )

    st.markdown(
        """
        ### Skills
        - Programming Languages: Python, R
        - Language: English, Mandarin
        - Database: SQL
        - Data Visualization: Tableau
        - Communication: Presentation Skills, Technical Writing
        - Adobe: Photoshop, Premiere
        """
    )

    st.markdown("---")
    
    # Interactive component has been moved to the experience page 