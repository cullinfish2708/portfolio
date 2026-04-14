import streamlit as st
import os
import base64
import streamlit.components.v1 as components

st.set_page_config(page_title="AJ Portfolio", page_icon="✨", layout="wide")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Projects", "Resume", "Contact"])

if page == "Home":
    st.title("Ajayamsavasan Arulmurugan")
    st.subheader("B.Tech Computer Science and Engineering Student | AI + IoT Builder")

    st.markdown("Building intelligent systems that connect software, hardware, and real-world problems")

    st.subheader("About Me:")
    st.write(
        "I am a B.Tech Computer Science and Engineering student with a strong interest in Artificial Intelligence, IoT, and real-world system design. "
        "I focus on building practical projects that combine software and hardware, such as smart automation systems using ESP32, sensors, and IoT platforms.\n\n"
        "I have experience working with Python, C/C++, and Java, along with web technologies like HTML, CSS, and JavaScript. "
        "My work often involves integrating multiple technologies such as embedded systems, cloud platforms, and user interfaces to create efficient and scalable solutions.\n\n"
        "I am particularly interested in developing intelligent systems that can learn from data and adapt to user behavior. "
        "Currently, I am exploring machine learning concepts and working towards building projects that go beyond basic automation into adaptive and predictive systems.\n\n"
        "I continuously improve my skills through hands-on projects, problem-solving, and learning new technologies, aiming to build impactful solutions in AI, IoT, and software development."
    )

    st.divider()

    st.subheader("🎓 Education:")
    st.markdown("""
B.Tech – Computer Science and Engineering  
SRM Institute of Science and Technology  
Expected Graduation: July 2028  
  

Class 12 (CBSE) 
Alpha Wisdom Vidyashram, Trichy  
Year: 2024  

Class 10 (CBSE)  
Alpha Wisdom Vidyashram, Trichy  
Year: 2022  
""")

    st.divider()

    st.subheader("💼 Internships:")
    st.markdown("""
Virtual Internship – CodeAlpha -
Duration: 10 July 2025 – 10 August 2025  

Data Science Virtual Internship – Edufyi Tech Solutions -
Duration: 01 September 2025 – 01 November 2025  
""")

elif page == "Projects":
    st.header("Projects:")

    with st.container():
        st.subheader("1. AI News Aggregator:")
        st.write(
            "An AI-powered news aggregator designed to collect, organize, and present news from multiple sources. "
            "It reduces information overload by filtering and grouping news based on relevance and user interest."
        )
        st.write(
            "This project combines machine learning, data processing, and networking concepts to build a smarter way of consuming news."
        )
        st.markdown("Tools Used: Python, Machine Learning, APIs/Web Scraping, Networking, GitHub")
        st.divider()

    with st.container():
        st.subheader("2. Page Replacement Simulator:")
        st.write(
            "A simulator that demonstrates memory management algorithms like FIFO, LRU, and Optimal replacement. "
            "It visualizes how pages are loaded and replaced in memory."
        )
        st.write("This project strengthened my understanding of operating systems and algorithm design.")
        st.markdown("Tools Used: Python / Java / C++, Data Structures, OS Concepts, GitHub")
        st.divider()

    with st.container():
        st.subheader("3. Smart IoT Blind Navigation System:")
        st.write(
            "An IoT-based assistive system designed to help visually impaired users navigate safely using sensors and real-time alerts."
        )
        st.write(
            "This project focuses on accessibility through embedded systems, sensor integration, and wireless communication."
        )
        st.markdown("Tools Used: ESP32 / Arduino, Ultrasonic Sensors, Buzzer/Vibration, C/C++, IoT Platforms")
        st.divider()

    with st.container():
        st.subheader("4. Smart Agriculture System (Ongoing):")
        st.write(
            "A smart agriculture system that uses sensors and IoT to monitor environmental conditions and automate farming tasks."
        )
        st.write(
            "This project focuses on real-time monitoring, automation, and improving efficiency in agriculture."
        )
        st.markdown("Tools Used: ESP32 / Arduino, Soil Moisture Sensor, DHT Sensor, IoT Platforms, Wi-Fi")


elif page == "Resume":
    st.header("📄 Resume")

    st.link_button("⬇️ Download Resume", "YOUR_GOOGLE_DRIVE_LINK")

    st.markdown("### 👀 Preview")

    st.markdown("""
    <iframe src="https://drive.google.com/file/d/FILE_ID/preview" 
    width="100%" height="700px"></iframe>
    """, unsafe_allow_html=True)

elif page == "Contact":
    st.header("Contact:")
    st.write("📧 Email: as0877@srmist.edu.in")
    st.write("📱 Mobile: +91 8754133567")
