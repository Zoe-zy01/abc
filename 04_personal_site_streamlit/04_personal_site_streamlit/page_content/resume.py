import streamlit as st
import base64
import os

def resume_page():
    pdf_file_path = os.path.join("static", "docs", "resume.pdf")

    if os.path.exists(pdf_file_path):
        with open(pdf_file_path, "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        # Display the download button
        st.download_button(label="Download Resume",
                        data=PDFbyte,
                        file_name="Ziyi_Zoe_Wang_Resume.pdf",
                        mime='application/octet-stream')
    else:
        st.warning("Resume PDF file not found")

    st.title("Ziyi Zoe Wang")

    st.header("Contact Information")
    st.markdown("""
    - **Email**: [ziyi.wang1@outlook.com](mailto:ziyi.wang1@outlook.com)
    - **Phone**: +86 18717718681
    - **LinkedIn**: [linkedin.com/in/ziyi-wang-18015b332](https://linkedin.com/in/ziyi-wang-18015b332)
    - **Address:** 607, Block C, Jueshi Mansion, Luohu District, Shenzhen, Guangdong, China
    """)

    st.header("Professional Summary")
    st.markdown("""
    A result-oriented MSc Marketing student at The Chinese University of Hong Kong (2024-2025), leveraging handson experience in digital marketing, data analytics, and omnichannel campaign execution across top-tier platforms (Meituan, POIZON, Kotex).
    """)

    st.header("Work Experience")
    st.markdown("""
    **Activity & Product Operations Intern, Dianping, Meituan** 
    - *April 2024 - July 2024*
    - Spearheaded 50% merchant acquisition for ”Must-Eat Festival,” exceeding KPIs by 110% via IVR/SMS campaigns and SQL-driven data review.
    - Designed a tiered interview framework for 152 merchants, improving retention rate by 12.8%.
    - Created concepts for the new product with 20% utilization rate. Executed holiday campaigns (e.g., Dragon Boat Festival) targeting 60k+ merchants, achieving 2M+ exposure.

    **Luxury & Sport Operations Intern, POIZON**
    - *January 2024 - April 2024*
    - Onboarded 58 premium brands (e.g., Arc'teryx, lululemon), optimizing product listings to lift 7-day GMV by up to 280%.
    - Daily interfaced with 10+ merchants, managed 35 product listings/optimizations per day, and enhanced merchant product vitality by 17.28% through data-driven pricing adjustments and SKU refinements.
    - Leaded merchants to sign up for 6 high-impact promotional events, increasing merchant participation by 40%.
    
     **Marketing Intern, Kotex, Kimberly-Clark (China) CO., Ltd**
    - *September 2023 - January 2024*
    - Orchestrated D11/Christmas campaigns across 5 O2O platforms, boosting brand search volume by 35%.
    - Drove 16-SKU product upgrades through competitor benchmarking and consumer testing, driving sales to 120% in the first month of new product launch.
    - Responsible for the supplier and CRM system, using Nielsen to complete the Q3 business tracking in 2023. 
    """)

    st.header("Education")
    st.markdown("""
    **Master of Marketing**
    - Chinese University of Hong Kong
    - *Graduated: October 2025*
    - GPA: 3.5/4.0
                
    **Bachelor of Economics**
    - Communication University of China
    - *Graduated: June 2023*
    - GPA: 3.76/4.0            
    """)

    st.header("Skills")
    st.markdown("""
    - **Programming Languages:** Python, R
    - **Language:** English, Mandarin
    - **Databases:** MySQL
    - **Adobe:** Photoshop, Premiere
    - **Soft Skills:** Team Leadership, Project Management, Problem-Solving, Communication
    """)

    st.header("Certifications")
    st.markdown("""
    - L'Oréal BRANDSTORM Top 400 in Greater China
    - Second Prize of the 12th Zhengda Cup National University Students’ Market Research and Analysis Competition of Beijing 
    """)

    st.header("Languages")
    st.markdown("""
    - **English:** Proficient
    - **Chinese:** Native
    """)

    st.header("Interests")
    st.markdown("""
    - Vlogging
    - Hiking
    """)

    st.markdown("---") 