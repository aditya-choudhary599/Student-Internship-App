import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="About the app",
    page_icon="1️⃣",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

if st.session_state["add_photo"] == True:
    with st.sidebar:
        st.image(Image.open('Part_C/Resources/student.jpg'),
                 caption=st.session_state["caption_of_photo"])
        st.session_state["retain_photo"]=True


title_container = st.container()
title_container.markdown(
    "<h1 style='text-align: center;'><u>About the app</u></h1>", unsafe_allow_html=True)

col1, col2 = st.columns([3, 4])

with col1:
    st.image(Image.open("Part_C/Resources/internship.jpg"),
             use_column_width=True)

with col2:
    st.write("Internships are an essential part of an engineering student's life as they offer valuable learning opportunities, industry exposure, and the chance to build a network of professional contacts. But many a times when we are studying in our first year or second year of engineering we are not aware of what skillsets are required by the companies. So using this app you will be able derive insightful analysis of what skillsets are required by the company. Here all the data is been colllected from the compnaies that will be visiting campus for offering the internships.")

    st.warning("🛑Note that this app is only for the Second Year Computer Engineering Students of COEP")

st.divider()

st.header("🔗🤔How to use this app ❓")

st.markdown("<div> <ol type=\"I\"><li>First you need to sign up for the app. You need to enter your MIS no and the college email id. Then you will be receiving the key to use the app on your college mail id. Please enter the same to proceed forward.</li><li>In the overall data analysis page you will be able to see the generalized plots of all the factors that are important for the internship.</li><li>In the domain specific page you can see the domain-specific data after applying the filters.</li><li>Here in the roadmap page you can find the roadmaps for learning various skills as well.</li><li>After you finish seeing all the things and you click on main page app you will be automatically logged out and will need to sign in again.</li></ol></div>", unsafe_allow_html=True)

st.divider()
