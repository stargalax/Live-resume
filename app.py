import streamlit as st
import plotly.graph_objects as go


st.set_page_config(page_title="Nikitha S | Portfolio", layout="wide")

# ---------- Sidebar Navigation -----------
st.markdown("""
    <style>
        .block-container {
            padding-top: 2rem;
        }
        .stTabs [data-baseweb="tab"] {
            font-size: 1rem;
            font-weight: 600;
        }
    </style>
""", unsafe_allow_html=True)

# ---------- Tabs -----------
tabs = st.tabs(["🏠 Home", "📜 Certifications", "💡 Projects", "🧭 Statement"])

# ---------- HOME -----------
with tabs[0]:
    st.title("Nikitha S")
    st.subheader("Final Year CS Student | Data & AI Enthusiast")
    cert_links = st.secrets["certifications"]

    col1, col2 = st.columns([1, 3])
    with col1:
        email = st.secrets["general"]["email"]
        github = st.secrets["general"]["github"].strip()  # remove accidental space
        linkedin = st.secrets["general"]["linkedIn"]

    st.markdown(f"""
    📍 Chennai, Tamil Nadu  
    📧 [Email](mailto:nikitha.s.2022.cse@ritchennai.edu.in)  
    🔗 [GitHub]({github}) | [LinkedIn]({linkedin})
    """)


    st.markdown("---")
    st.markdown("### 🧠 Profile Summary")
    st.info("""
    Final-year CS student with a passion for solving real-world problems using data-driven models. 
    Experienced in deep learning, automation, and predictive analytics. Skilled in developing interactive 
    data tools and applying ML techniques to extract business insights and simulate policy outcomes.
    """)

    st.markdown("### 🎓 Education")
    st.success("""
    **B.E. Computer Science and Engineering**  
    Rajalakshmi Institute of Technology, Chennai (20222026)  
    """)

    st.markdown("### 🛠️ Skills")
    st.markdown("""
    - **Programming**: Python, MySQL, HTML/CSS, JavaScript (Basic)  
    - **Libraries**: TensorFlow, OpenCV, Streamlit, Pandas, NumPy  
    - **Tools**: Google Colab, Firebase, GitHub, Excel  
    - **Concepts**: Deep Learning, OCR, Data Analysis, Predictive Modeling, Simulation  
    - **Soft Skills**: Analytical Thinking, Communication, Curiosity, Self-learning
    """)

    
    st.markdown("### ✅ Certifications")
    st.markdown(f"""
    - Deep Learning – NVIDIA  
    - Python for Data Science – IBM  
    - Web Scraping – Simplilearn  
    - [Excel Essentials – LinkedIn Learning]({cert_links.excel})  
    - Data Fundamentals – IBM SkillsBuild  
    - [Analytics Engineering Project – LinkedIn Learning]({cert_links.analytics_eng})
    - [Oracle SQL Explorer - Oracle University]({cert_links.sql})
    - [ML]
    """)

    st.markdown("### 💼 Experience")
    st.warning("""
    **Intern – SharePoint Designs** (Feb 2025 – Present)  
    Created modular SPFx web parts using React and PnPjs. Built enterprise-grade internal dashboards and 
    automated list-driven components.
    """)

# ---------- CERTIFICATIONS (Progress) -----------
with tabs[1]:
    st.header("📊 Certifications In Progress")
    #st.write("Hover or tap to view dashboard links")

    import numpy as np
    st.markdown("""
    <style>
    .block-container {
        padding-top: 2rem;
    }
    .stTabs [data-baseweb="tab"] {
        font-size: 1rem;
        font-weight: 600;
    }
    /* ✨ Fix Plotly hover cursor to default */
    .js-plotly-plot .plotly .cursor-crosshair {
        cursor: default !important;
    }
    </style>
""", unsafe_allow_html=True)


    # Percent completion values
    values = [40, 50,30]
    labels = ["Oracle Data Platform", "IBM Python", "ML Foundations-AWS Educate"]
    colors = ['#FF6B6B', '#4CAF50', '#2196F3']
    links = [
        st.secrets["certifications"]["oracle_dashboard"],
        st.secrets["certifications"]["ibm_dashboard"],
        st.secrets["certifications"]["ml_foundation"]
    ]

    fig = go.Figure()

    for i, (v, label, color, link) in enumerate(zip(values, labels, colors, links)):
        theta = np.linspace(0, v * 3.6, 100)
        r_base = 0.5 + i * 0.2
        r = np.full_like(theta, r_base)

        fig.add_trace(go.Scatterpolar(
            r=r,
            theta=theta,
            mode='lines',
            line=dict(color=color, width=14),
            hovertemplate=f"{label}: {v}",
            name=label,
            showlegend=False
        ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=False, range=[0, 1.5]),
            angularaxis=dict(visible=False)
        ),
        showlegend=False,
        height=500,
        margin=dict(t=20, b=20, l=0, r=0),
    )

    st.plotly_chart(fig, use_container_width=True)

    # Optional: fallback text links
    st.markdown("""
    - 🔴 [Oracle Certification Dashboard](%s)  
    - 🟢 [IBM Python Dashboard](%s) 
    - 🟣 [ML Foundation by AWS Educate](%s) 
    """ % tuple(links))
    


# ---------- PROJECTS -----------
with tabs[2]:
    st.header("🚀 Key Projects")
    st.markdown("""
    #### 🧠 Crowd Safety Prediction Tool
    Detects crowd surges using deep learning. Flags stampede risks in real time.

    #### 🗺️ Public Sector Data Insights
    Tourism dashboard using Snowflake + open data.
    [Live App](https://your-story-challenge-xzr2gcxdge2jd27rztbhae.streamlit.app/) | 
    [Presentation Deck](https://gamma.app/docs/Public-Sector-Strategy-Support-using-Tourism-Insights-69tfbla4xwdxkry)

    #### 📦 Dataset Curation Automation Tool
    UI-based image scraper & ML dataset packager. 
    [Live App](https://webscrapp-lcfhxdvwcvadycsp9ff9fy.streamlit.app/)

    #### 📝 Japanese OCR
    Built handwritten character recognition system for Hiragana/Katakana using EasyOCR.

    #### 📊 Policy Impact Simulation Tool (Ongoing)
    Interactive "what-if" model builder for government policy planners.
    """)

# ---------- STATEMENT -----------
with tabs[3]:
    st.header("🧭 Personal Statement")
    st.success("""
        I enjoy crafting user experiences that make data more accessible, meaningful, and actionable.  
        My goal is to help individuals and organizations make informed, data-driven choices through intuitive design, powerful analytics, and thoughtful storytelling.  
        Whether it's through dashboards, simulations, or predictive tools, I aim to turn complexity into clarity.
This website is a passion project I built not only to showcase my work but also to explore the boundaries of how data can be experienced. I believe the power of information lies not just in numbers, but in how clearly and creatively it can be communicated. From certifications in progress to experimental AI tools, everything you see here reflects my curiosity, continuous growth, and desire to make an impact ; one percent everyday.
    """)
