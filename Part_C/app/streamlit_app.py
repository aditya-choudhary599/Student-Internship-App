import streamlit as st
import json
import pyrebase
from PIL import Image


def getname(email_id, temp_dict):
    for key in temp_dict:
        if temp_dict[key]["Coep MailId"] == email_id:
            return temp_dict[key]["Student Name "]
    return


firebase_dict = json.loads(st.secrets["textkey3"])
firebase = pyrebase.initialize_app(firebase_dict)

st.set_page_config(
    page_title="SY STUDENT INTERNSHIP DATA",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)


title_container = st.container()
title_container.markdown(
    "<h1 style='text-align: center;'><u>👨‍💻Welcome to the SY COMP INTERNSHIP DATA👩‍💻</u></h1>", unsafe_allow_html=True)

temp_dict = json.loads(st.secrets["textkey2"])

tab1, tab2 = st.tabs(["Sign up", "Log in"])

with tab1:
    st.markdown(
        "<h2 style='text-align: center;'><u>Sign up</u></h1>", unsafe_allow_html=True)
    mis = st.text_input("**Enter your Mis no.**")
    if mis:
        if mis not in temp_dict:
            st.error("❌You are not a Student of SY Computer Engineering COEP")
        else:
            st.success("✅You are the Student of SY Compueter Engineering")
            st.info(
                "Now to use this app you need to register using your college mail Id. Please complete the follwoing steps.")
            sign_up_email_id = st.text_input(
                "**Enter your college email Id**", value=temp_dict[mis]["Coep MailId"], disabled=True)

            sign_up_password = st.text_input(
                "**Set a new password**", type='password')

            if sign_up_password:
                confirm_sign_up_password = st.text_input(
                    "**Confirm the password**", type='password')
                if confirm_sign_up_password:
                    if confirm_sign_up_password != sign_up_password:
                        st.error("❌Wrong Password")
                        st.stop()
                    else:
                        st.success("✅Correct Password")

                    sbt_btn = st.button(label='**Submit**')

                    if sbt_btn:
                        try:
                            sign_up = firebase.auth().create_user_with_email_and_password(
                                sign_up_email_id, sign_up_password)
                            st.success(
                                "✅Entry added succesfully in the database.")
                            st.info(
                                "Now you can use this credentials to log in to the app")
                        except Exception as e:
                            # displaying the error log
                            helper = (e.args[1])
                            ee = json.loads(helper)
                            st.error(ee["error"]["message"], icon='❌')

with tab2:
    st.markdown(
        "<h2 style='text-align: center;'><u>Log in</u></h1>", unsafe_allow_html=True)

    log_in_email_id = st.text_input("**Enter your college email id**")
    st.session_state['add_photo'] = False
    if log_in_email_id:
        log_in_password = st.text_input(
            "**Enter your password**", type='password')
        if log_in_password:
            try:
                login = firebase.auth().sign_in_with_email_and_password(
                    log_in_email_id, log_in_password)
                st.success("✅Successfully logged in")
                st.session_state['add_photo'] = True
            except:
                st.error("❌Invalid Credentials")
                st.stop()

if st.session_state["add_photo"] == True:
    with st.sidebar:
        st.image(Image.open('Part_C\Resources\student.jpg'),
                 caption=getname(log_in_email_id, temp_dict))
        st.session_state["caption_of_photo"] = getname(
            log_in_email_id, temp_dict)
        st.session_state["retain_photo"] = True
