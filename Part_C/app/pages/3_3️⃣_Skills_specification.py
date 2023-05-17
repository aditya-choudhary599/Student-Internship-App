import streamlit as st
import pandas as pd
from PIL import Image

st.set_page_config(
    page_title="Skills specifications",
    page_icon="3️⃣",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)


def data_shower(student_sex: str, student_curr_cgpa: float, student_required_domain: str,student_active_backlogs:int,student_dead_backlogs:int) -> None:
    st.subheader("🔗For the selected options,here are comapnies for you.")
    if student_required_domain == '🌐Web Development':
        df = pd.read_csv('Part_B/Final_Data/Final_web_dev_data.csv')

    elif student_required_domain=="📱Mobile App Development":
        df=pd.read_csv('Part_B/Final_Data/Final_app_dev_data.csv')

    elif student_required_domain=="📈Data Science and Analytics":
        df=pd.read_csv('Part_B/Final_Data/Final_data_sci_data.csv')

    elif student_required_domain=='🧠Artificial Intelligence and Machine Learning':
        df=pd.read_csv('Part_B/Final_Data/Final_aiml_data.csv')

    elif student_required_domain=='☁️Cloud Engineer':
        df=pd.read_csv('Part_B/Final_Data/Final_cloud_data.csv')

    elif student_required_domain=='🔢Database Engineer':
        df=pd.read_csv('Part_B/Final_Data/Final_dbms_data.csv')

    elif student_required_domain=='👨‍💻Devops Engineer':
        df=pd.read_csv('Part_B/Final_Data/Final_devops_data.csv')
    
    else:
        df=pd.read_csv('Part_B/Final_Data/Final_cs_data.csv')

    df = df.drop(['Unnamed: 0'], axis=1)
    if student_sex == '👦Male':
        df = df.drop(['Seats for Girls'], axis=1).query(
            '`Seats for Boys`>0').reset_index(drop=True)
    else:
        df = df.drop(['Seats for Boys'], axis=1).query(
            '`Seats for Girls`>0').reset_index(drop=True)

    df = df.query('`Min CGPA` <= @student_curr_cgpa and `Number of Dead Backlogs permitted` >= @student_active_backlogs and `Number of Active Backlogs permitted` >= @ student_dead_backlogs').reset_index(drop=True)

    st.dataframe(df)

        


if st.session_state["add_photo"] == True:
    with st.sidebar:
        st.image(Image.open('Part_C/Resources/student.jpg'),
                 caption=st.session_state["caption_of_photo"])

    title_container = st.container()
    title_container.markdown(
        "<h1 style='text-align: center;'><u>Skills specifications</u></h1>", unsafe_allow_html=True)

    st.divider()

    student_sex = st.radio(label='**➡️Select your Gender**',
                           options=["👦Male", "👧Female"])

    student_curr_cgpa = st.number_input(
        label='**➡️Enter your current CGPA**', min_value=6.0, max_value=10.0, step=0.1)

    col1, col2 = st.columns(2)

    with col1:
        student_active_backlogs = st.number_input(
            label='**➡️Enter number of your active backlogs**', min_value=0, max_value=2, step=1)

    with col2:
        student_dead_backlogs = st.number_input(
            label='**➡️Enter number of your dead backlogs**', min_value=0, max_value=2, step=1)

    student_required_domain = st.selectbox(label="➡️**Select the preferred domain:**", options=["🌐Web Development", "📱Mobile App Development", "📈Data Science and Analytics",
                                           "🧠Artificial Intelligence and Machine Learning", "☁️Cloud Engineer", "🔢Database Engineer", "👨‍💻Devops Engineer", "🕵🏻Cyber Security"])

    sbt_btn = st.button(label='Submit')

    if sbt_btn:
        st.divider()
        data_shower(student_sex, student_curr_cgpa, student_required_domain,student_active_backlogs,student_dead_backlogs)
