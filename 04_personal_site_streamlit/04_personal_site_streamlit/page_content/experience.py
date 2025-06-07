import streamlit as st
from PIL import Image
import os

def experience_page():
    st.markdown("## Professional Experience")
    
    col1, col2 = st.columns([3, 1])

    with col1:
     st.markdown("""
    ### Activity & Product Operations Intern
    **Dianping, Meituan** | *April 2024 - July 2024*
    - Overheaded 50% merchant acquisition for ”Must-Eat Festival,” exceeding KPIs by 110% via IVR/SMS campaigns and SQL-driven data review.
    - Designed a tiered interview framework for 152 merchants, improving retention rate by 12.8%.
    - Created concepts for the new product with 20% utilization rate. Executed holiday campaigns (e.g., Dragon Boat Festival) targeting 60k+ merchants, achieving 2M+ exposure.
    """)
    
    with col2:
        # 添加图片
        image_path = os.path.join("static", "images", "dianping.jpg")
        if os.path.exists(image_path):
            image = Image.open(image_path)
            st.image(image, width=150)
        else:
            st.warning("Company image not found")

    col1, col2 = st.columns([3, 1])
    with col1:        
     st.markdown("""
    ### Luxury & Sport Operations Intern
    **POIZON** | *January 2024 - April 2024*
    
    - Onboarded 58 premium brands (e.g., Arc’teryx, lululemon), optimizing product listings to lift 7-day GMV by up to 280%.
    - Daily interfaced with 10+ merchants, managed 35 product listings/optimizations per day, and enhanced merchant product vitality by 17.28% through data-driven pricing adjustments and SKU refinements.
    - Leaded merchants to sign up for 6 high-impact promotional events, increasing merchant participation by 40%.
    """)
    
    with col2:
        # 添加图片
        image_path = os.path.join("static", "images", "dewu.jpg")
        if os.path.exists(image_path):
            image = Image.open(image_path)
            st.image(image, width=150)
        else:
            st.warning("Company image not found")
            
    col1, col2 = st.columns([3, 1])
    with col1:
     st.markdown("""
    ### Marketing Intern
    **Kotex, Kimberly-Clark (China) CO., Ltd** | *September 2023 - January 2024*
    
    - Orchestrated D11/Christmas campaigns across 5 O2O platforms, boosting brand search volume by 35%.
    - Drove 16-SKU product upgrades through competitor benchmarking and consumer testing, driving sales to 120% in the first month of new product launch.
    - Responsible for the supplier and CRM system, using Nielsen to complete the Q3 business tracking in 2023.
    """)
    
    with col2:
        # 添加图片
        image_path = os.path.join("static", "images", "kotex.png")
        if os.path.exists(image_path):
            image = Image.open(image_path)
            st.image(image, width=150)
        else:
            st.warning("Company image not found")

    st.markdown("---")
    
    st.markdown("## Campus Experience")
    
    st.markdown("""
    ### Head
    **Promotion Department, Student Union** | *September 2019 - June 2021*
    
    - Designed posters and brochures with Photoshop and school magazine with InDesign, wrote on average 30+ articles each year with over 6,000 reads.
    - Planned and executed the academy’s ”Breathe” three-line poem event as an activity leader.
    """)
    
    st.markdown("---")
    
    st.markdown("## Professional Skills")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Technical Skills
        - **Programming Languages:** Python, R, SQL
        - **Data Processing:** Pandas, NumPy, PySpark
        - **Visualization:** Matplotlib, Seaborn, Tableau, PowerBI
        """)
        
    with col2:
        st.markdown("""
        ### Soft Skills
        - **Communication:** Excellent written and verbal communication
        - **Teamwork:** Collaborative team player with experience in Agile environments
        - **Problem-solving:** Strong analytical and critical thinking abilities
        - **Time Management:** Efficient at prioritizing tasks and meeting deadlines
        - **Leadership:** Experience leading small teams and mentoring junior colleagues
        - **Adaptability:** Quick learner who thrives in dynamic environments
        """)
    
    st.markdown("---") 