import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image
from pathlib import Path
from streamlit_lottie import st_lottie

PAGE_TITLE = "Portfolio | PRASHANTH NAVUGAPU"
PAGE_ICON = ":wave:"

st.set_page_config(layout="wide",page_title=PAGE_TITLE, page_icon=PAGE_ICON)

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
resume_file = current_dir / "assets" / "Prashanth Resume au.pdf"
css_file = current_dir / "styles" / "main.css"
EMAIL = "work.nprashanth@gmail.com"

SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/nprashanth1712/",
    "GitHub": "https://github.com/nprashanth1712"

}

def loadUrl(url):
    response=requests.get(url)
    if response.status_code!=200:
        return None
    return response.json()

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()


coder= loadUrl("https://lottie.host/120d4a92-ef4c-4b54-8d52-f965069e45ba/L8meiSr4kh.json")
contact_us= loadUrl("https://lottie.host/50af316e-8f92-46c2-94d3-ca354369d1a4/5oPpKCzznQ.json")
profile_pic = loadUrl("https://lottie.host/29721b90-34fe-4554-bf91-0391f38ed6c9/kRoX3IZIw2.json")



col1,col2=st.columns((2,1))
with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Hello World!!! :wave:")
            st.header("""I am Prashanth, """)
            st.subheader("Navigating the Nexus of Data and AI :)")
            st.write("##")
            st.download_button(
            label=" 📄 Download Resume",
            data=PDFbyte,
            file_name=resume_file.name,
            mime="application/octet-stream",
             )
            st.write("📫", EMAIL)
            st.write('\n')
            cols = st.columns(len(SOCIAL_MEDIA))
            for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
                cols[index].write(f"[{platform}]({link})")
            with col2:
             st_lottie(profile_pic,height=300)
st.write("##")


st.write("---")

with st.container():
    selected=option_menu(
        menu_title=None,
        options=['About','Projects','Contact'],
        icons=['person','code-slash','chat-left-text-fill'],
        orientation='horizontal'
        )
if selected =='About':
    with st.container():
        col3, col4 = st.columns(2)
        with col3:
            st_lottie(coder)
        with col4:
            st.write('##')
            st.write("""## Unveiling My Arsenal 

Here's a glimpse of what I bring to the tech table:

👷 A.I. System / RAG Builder
                     
🐍 Python Power

🔮 Machine Learning Magician

📊 Data Sorcery

🌐 Web Wizardry

🔧 Problem-Solving Sorcerer

🎨 Art of Visualization
                     
🛠️ Project Alchemist
                     
🎯 Product Strategy Sage
                     
🧩 Management Maestro

🚀 Lifelong Learner

So, let's embark on a magical journey together and witness the wonders we can create with technology!
""")
            
    st.write("---")  
    with st.container():
        st.header('Work Experiences :')
        st.write("##")
        st.subheader("""
►Freelancing (A.I./Consulting)
    Time Period :  OCT, 2023 - PRESENT
    India · Remote
                     
    AI-Based Astrology Chatbot app:
    Objective: Created an AI-based astrology app leveraging the OpenAI Assistant API. Developed a Retrieval-Augmented Generation (RAG) system trained on Hindu astrological texts. 
    Took responsibility for managing the AI development, while collaborating with external teams for API integration and interface design.
                     
    2D to 3D NFT Image Conversion Using AI:

    Objective: Developed a solution for converting 2D images into 3D NFTs.
    Approach: Implemented advanced AI techniques to enhance visual quality.
    Responsibilities: Led the AI development and coordinated with the team for interface integration and design.
                     
    Web Design and Development for Maalaxmi.ai:

    Objective: Designed and developed a user-friendly website for Maalaxmi.ai.
    Approach: Integrated AI functionalities and managed the project from concept to launch.
    Responsibilities: Directed design and development, ensuring alignment with client requirements.
                     
    Key Responsibilities Across Projects:

    AI Component Management: Implemented cutting-edge technologies and algorithms.
    Project Management: Oversaw client meetings, hiring, and team management.
    Coordination: Worked with external teams for specialized tasks such as interface integration and design.
    Quality and Timeliness: Ensured projects were delivered on time with high standards of quality and accuracy
                     """)  
        st.write("##")
        st.write("##")
        st.subheader("""
►DATA SCIENCE / ML
    - DATA SCIENCE/A.I./M.L. TRAINER @ Anion SOFTECH 
    - Time Period : Feb 2022 - Sep 2023 
    - India · Hybrid
    - Conducted workshops and seminars on AI, ML, and data science for students, faculty, and industry professionals 
    - Worked with cross-functional teams to develop and implement data-driven solutions to real world business problems 
    - Analyzed large datasets to uncover hidden trends and insights using statistical techniques · Built predictive models to forecast customer behavior and sales trends 
    - Designed and implemented advanced analytics and machine learning algorithms to automate complex business processes

    """)
        st.write("##")
        st.write("##")
        st.subheader("""
►DATA SCIENCE / ML
    - Internship @ Anion SOFTECH 
    - Time Period : Jan 2021 - Jan 2022 
    - India · Hybrid
    - Assisted in the development of predictive models using machine learning algorithms to optimize the learning experience of students.
    - Conducted exploratory data analysis to identify patterns and trends in student behavior.
    - Designed and implemented interactive dashboards using Power B.I to visualize student performance and engagement metrics.
    - Collaborated with cross-functional teams to identify and implement data-driven solutions to improve student outcomes.

                     """)
    st.write("---")  
    st.write("---") 
#     with st.container():
#         st.header('Education :') 
#         st.subheader("""
# ►BMS COLLEGE OF ENGINEERING
#     -B.TECH @ ELECTRONICS AND COMMUNICATIONS ENGINEERING
#     -Time Period : 2021-2025
#     -Bengaluru, Karnataka, India 
#     - CGPA - 8.05
#     -I have participated in various hackathons, in which I developed various projects like SecureProX and BookWise (more details
#     about these projects are available in projects section) 
#                      """) 



if selected == 'Projects':
    with st.container():
        st.header('MY Projects')
        st.write('##')
        st.subheader(f"[🏆 LaxmiAstroAI](https://drive.google.com/file/d/1ey1_Lb-3jqq0oO2VHm76YBpypG33vbCs/view?usp=drivesdk)")
        st.write(f"[LaxmiAstroAI is an advanced AI-powered astrology app designed to provide personalized astrological insights based on the ancient wisdom of Hindu Vedic texts. By integrating cutting-edge AI technology, including a Retrieval-Augmented Generation (RAG) system and various astrology APIs, LaxmiAstroAI offers accurate and culturally authentic guidance tailored to individual user queries](https://drive.google.com/file/d/1ey1_Lb-3jqq0oO2VHm76YBpypG33vbCs/view?usp=drivesdk)")
        
        st.write('##')
        
        st.subheader(f"[🏆Laxmi-m website ](https://laxmi-m.com/)")
        st.write(f"[Laxmi-m.com is a website designed and developed for one of my clients, showcasing a seamless blend of functionality and aesthetic appeal. The project involved creating a user-friendly interface with a responsive design, ensuring smooth navigation across devices. The website is optimized for performance, delivering a high-quality user experience while maintaining modern design standards. It integrates various features to meet the client’s needs, highlighting my team's expertise in web development and design](https://laxmi-m.com/)")
        
        st.write('##')
       
        st.subheader(f"[🏆 2D to 3D nft image conversion](https://nft.maalaxmi.ai/)")
        st.write(f"[This functionality, which we developed as a core part of the website, allows users to transform traditional 2D images into immersive 3D NFT assets. Leveraging AI and stable diffusion algorithms, the system generates high-quality 3D representations, enhancing user creativity and interaction within the NFT space. The NFT conversion feature is seamlessly integrated with the website’s user interface, offering a smooth, intuitive experience for artists and collectors alike. This project demonstrates our ability to fuse cutting-edge AI technology with web development to create a highly interactive platform for the evolving NFT market.](https://nft.maalaxmi.ai/)")
        
        st.write('##')
       
        st.subheader(f"[🏆 Maa Laxmi ai website](https://maalaxmi.ai/)")
        st.write(f"[maalaxmi.ai is a website designed and developed for one of my clients, showcasing a seamless blend of functionality and aesthetic appeal. The project involved creating a user-friendly interface with a responsive design, ensuring smooth navigation across devices. The website is optimized for performance, delivering a high-quality user experience while maintaining modern design standards. It integrates various features to meet the client’s needs, highlighting my team's expertise in web development and design](https://maalaxmi.ai/)")
        
        st.write('##')

        st.subheader(f"[🏆 Other projects](https://github.com/nprashanth1712?tab=repositories)")
if selected=='Contact':
    st.header("Get In Touch")
    st.write('##')
    st.write('##')
    
    contact_form="""
  <form target="_blank" action="https://formsubmit.co/work.nprashanth@gmail.com" method="POST">
     <input type="text" name="name" class="form-control" placeholder="Enter Your Full Name"  required>
     
     <input type="email" name="email" class="form-control" placeholder="Enter Your Email Address"  required>   
     
    <textarea type="message" placeholder="Enter Your Message" class="text_area" name="input_message"  rows="10" required></textarea>
     
    <button type="submit" class="btn" >Send</button>
       
  </form>
    """
    left_col, right_col= st.columns((2,1))
    with left_col:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_col:
        st_lottie(contact_us, height=300)
        
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
