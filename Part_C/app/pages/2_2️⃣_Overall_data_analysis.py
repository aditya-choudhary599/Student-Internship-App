import streamlit as st
from PIL import Image
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Overall Data Analysis",
    page_icon="2️⃣",
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
    title_container = st.container()
    title_container.markdown(
    "<h1 style='text-align: center;'><u>Overall Data Analaysis</u></h1>", unsafe_allow_html=True)
    overall_df=pd.read_csv("Part_B/Final_Data/Final_overall_data.csv")
    st.header('🔗Company Domain Distribution')
    fig_1=px.histogram(overall_df,x='Domain to Hire',text_auto='auto',height=600)
    st.plotly_chart(fig_1,use_container_width=True)
    st.divider()

    st.header('🔗Minimum CGPA Requirements')
    fig_2=px.histogram(overall_df,x='Min CGPA',nbins=8,text_auto=True,color='Domain to Hire',height=600)
    st.plotly_chart(fig_2,use_container_width=True)
    st.divider()

    st.header('🔗Internships Seats Stats')
    fig_3=px.histogram(overall_df,y=['Seats for Boys','Seats for Girls'],text_auto=True,x='Domain to Hire',barmode='group',height=600)
    st.plotly_chart(fig_3,use_container_width=True)
    st.divider()

    st.header('🔗Company Active Backlogs permitted')
    fig_4=px.histogram(overall_df,x='Domain to Hire',color='Number of Active Backlogs permitted',text_auto=True,height=600,barmode='group')
    st.plotly_chart(fig_4,use_container_width=True)
    st.divider()

    st.header('🔗Company Dead Backlogs permitted')
    fig_5=px.histogram(overall_df,x='Domain to Hire',color='Number of Dead Backlogs permitted',text_auto=True,height=600,barmode='group')
    st.plotly_chart(fig_5,use_container_width=True)
    st.divider()

    st.header('🔗Company campus visiting month')
    fig_6=px.histogram(overall_df,color='Preffered month of visiting campus',text_auto=True,x='Domain to Hire',height=800)
    st.plotly_chart(fig_6,use_container_width=True)
    st.divider()

   

    
