import streamlit as st
from PIL import Image


def pdf_helper(pdf_file_path, download_file_name):
    with open(pdf_file_path, "rb") as pdf_file:
        PDFbyte = pdf_file.read()

    st.download_button(label="Download PDF",
                       data=PDFbyte,
                       file_name=f"{download_file_name}.pdf",
                       mime='application/octet-stream')


def image_helper(path_of_image_file: str):
    img = Image.open(path_of_image_file)
    aspect_ratio = 1.8

    # Calculate new size while preserving aspect ratio
    new_width = 500
    new_height = int(new_width / aspect_ratio)

    # Resize the image using Lanczos resampling
    img = img.resize((new_width, new_height), Image.LANCZOS)
    return img


st.set_page_config(
    page_title="Roadmaps",
    page_icon="4️⃣",
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
        st.image(Image.open('Part_C\Resources\student.jpg'),
                 caption=st.session_state["caption_of_photo"])
        
    title_container = st.container()
    title_container.markdown(
    "<h1 style='text-align: center;'><u>Roadmaps</u></h1>", unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["Role Based Roadmaps", "Skill Based Roadmap"])

    with tab1:
        with st.container():
            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.image(image_helper(
                    'Part_C\Resources\Roadmaps\Role_Based_Roadmaps\Photos\Android-App-Development-2.jpg'), use_column_width=True)
                pdf_helper('Part_C\Resources\Roadmaps\Role_Based_Roadmaps\Android.pdf',
                           'Android Development Roadmap')

            with col2:
                st.image(image_helper(
                    'Part_C\Resources\Roadmaps\Role_Based_Roadmaps\Photos\Aspnet-core-featured.png'), use_column_width=True)
                pdf_helper(
                    'Part_C\Resources\Roadmaps\Role_Based_Roadmaps\Aspnet-core.pdf', 'Aspnet-core Roadmap')

            with col3:
                st.image(image_helper(
                    'Part_C\Resources\Roadmaps\Role_Based_Roadmaps\Photos\Backend_development.jpg'))
                pdf_helper('Part_C\Resources\Roadmaps\Role_Based_Roadmaps\Backend.pdf',
                           'Backend Development Roadmap')

            with col4:
                st.image(image_helper(
                    'Part_C\Resources\Roadmaps\Role_Based_Roadmaps\Photos\Big-data-engineer.jpg'), use_column_width=True)
                pdf_helper(
                    'Part_C\Resources\Roadmaps\Role_Based_Roadmaps\Big_data_engineer.pdf', 'Big Data Engineer Roadmap')

        st.text("\n")
        st.text("\n")

        with st.container():
            col5, col6, col7, col8 = st.columns(4)

            with col5:
                st.image(image_helper(
                    'Part_C\Resources\Roadmaps\Role_Based_Roadmaps\Photos\Cyber_Security.jpg'), use_column_width=True)
                pdf_helper(
                    'Part_C\Resources\Roadmaps\Role_Based_Roadmaps\Cyber-security.pdf', 'Cyber Security Roadmap')

            with col6:
                st.image(image_helper(
                    'Part_C\Resources\Roadmaps\Role_Based_Roadmaps\Photos\Data_Engineering.jpg'), use_column_width=True)
                pdf_helper(
                    'Part_C\Resources\Roadmaps\Role_Based_Roadmaps\Data_engineer.pdf', 'Data Engineering Roadmap')

            with col7:
                st.image(image_helper(
                    'Part_C\Resources\Roadmaps\Role_Based_Roadmaps\Photos\Data_Science.jpg'), use_column_width=True)
                pdf_helper(
                    'Part_C\Resources\Roadmaps\Role_Based_Roadmaps\Datascience.pdf', 'Data Science Roadmap')

            with col8:
                st.image(image_helper(
                    'Part_C\Resources\Roadmaps\Role_Based_Roadmaps\Photos\Deep_Learningjpg.jpg'), use_column_width=True)
                pdf_helper(
                    'Part_C\Resources\Roadmaps\Role_Based_Roadmaps\Deep_learning.pdf', 'Deep Learning Roadmap')

        st.text("\n")
        st.text("\n")

        with st.container():
            col11, col12, col13, col14 = st.columns(4)

            with col11:
                st.image(image_helper(
                    'Part_C\Resources\Roadmaps\Role_Based_Roadmaps\Photos\Devops.jpg'), use_column_width=True)
                pdf_helper(
                    'Part_C\Resources\Roadmaps\Role_Based_Roadmaps\Devops.pdf', 'Devops Engineer Roadmap')

            with col12:
                st.image(image_helper(
                    'Part_C\Resources\Roadmaps\Role_Based_Roadmaps\Photos\Frontened_Dev.jpg'), use_column_width=True)
                pdf_helper(
                    'Part_C\Resources\Roadmaps\Role_Based_Roadmaps\Frontend.pdf', 'Frontend Developer Roadmap')

            with col13:
                st.image(image_helper(
                    'Part_C\Resources\Roadmaps\Role_Based_Roadmaps\Photos\Full_stack_dev.jpg'), use_column_width=True)
                pdf_helper('Part_C\Resources\Roadmaps\Role_Based_Roadmaps\Full-stack.pdf',
                           'Full Stack Developer Roadmap')

            with col14:
                st.image(image_helper(
                    'Part_C\Resources\Roadmaps\Role_Based_Roadmaps\Photos\\Ux_design.jpg'), use_column_width=True)
                pdf_helper(
                    'Part_C\Resources\Roadmaps\Role_Based_Roadmaps\\Ux-design.pdf', 'UX Design Roadmap')

    with tab2:
        with st.container():
            col15, col16, col17, col18 = st.columns(4)

            with col15:
                st.image(image_helper(
                    'Part_C\Resources\Roadmaps\Skill_Based_Roadmap\Photos\Angular.jpg'), use_column_width=True)
                pdf_helper(
                    'Part_C\Resources\Roadmaps\Skill_Based_Roadmap\Angular.pdf', 'Angular Learning Roadmap')

            with col16:
                st.image(image_helper(
                    'Part_C\Resources\Roadmaps\Skill_Based_Roadmap\Photos\Design_Sysytem.png'), use_column_width=True)
                pdf_helper('Part_C\Resources\Roadmaps\Skill_Based_Roadmap\Design-system.pdf',
                           'Design System Learning Roadmap')

            with col17:
                st.image(image_helper(
                    'Part_C\Resources\Roadmaps\Skill_Based_Roadmap\Photos\Docker.png'), use_column_width=True)
                pdf_helper(
                    'Part_C\Resources\Roadmaps\Skill_Based_Roadmap\Docker.pdf', 'Docker Learning Roadmap')

            with col18:
                st.image(image_helper(
                    'Part_C\Resources\Roadmaps\Skill_Based_Roadmap\Photos\Golang.jpg'), use_column_width=True)
                pdf_helper(
                    'Part_C\Resources\Roadmaps\Skill_Based_Roadmap\Golang.pdf', 'Golang Learning Roadmap')

        st.text("\n")
        st.text("\n")

        with st.container():
            col19, col20, col21, col22 = st.columns(4)

            with col19:
                st.image(image_helper(
                    'Part_C\Resources\Roadmaps\Skill_Based_Roadmap\Photos\Graph_ql.png'), use_column_width=True)
                pdf_helper(
                    'Part_C\Resources\Roadmaps\Skill_Based_Roadmap\Graphql.pdf', 'GraphQL Learning Roadmap')

            with col20:
                st.image(image_helper(
                    'Part_C\Resources\Roadmaps\Skill_Based_Roadmap\Photos\Java.jpg'), use_column_width=True)
                pdf_helper(
                    'Part_C\Resources\Roadmaps\Skill_Based_Roadmap\Java.pdf', 'Java Learning Roadmap')

            with col21:
                st.image(image_helper(
                    'Part_C\Resources\Roadmaps\Skill_Based_Roadmap\Photos\Javascript.png'), use_column_width=True)
                pdf_helper('Part_C\Resources\Roadmaps\Skill_Based_Roadmap\Javascript.pdf',
                           'Javascript Learning Roadmap')

            with col22:
                st.image(image_helper(
                    'Part_C\Resources\Roadmaps\Skill_Based_Roadmap\Photos\Kubernetes.jpg'), use_column_width=True)
                pdf_helper('Part_C\Resources\Roadmaps\Skill_Based_Roadmap\Kubernetes.pdf',
                           'Kubernetes Learning Roadmap')

        st.text("\n")
        st.text("\n")

        with st.container():
            col23, col24, col25, col26 = st.columns(4)

            with col23:
                st.image(
                    'Part_C\Resources\Roadmaps\Skill_Based_Roadmap\Photos\MongoDb.png', use_column_width=True)
                pdf_helper(
                    'Part_C\Resources\Roadmaps\Skill_Based_Roadmap\Mongodb.pdf', 'MongoDB Learning Roadmap')

            with col24:
                st.image(
                    'Part_C\Resources\Roadmaps\Skill_Based_Roadmap\Photos\\NodeJs.jpg', use_column_width=True)
                pdf_helper(
                    'Part_C\Resources\Roadmaps\Skill_Based_Roadmap\\Nodejs.pdf', 'NodeJS Learning Roadmap')

            with col25:
                st.image(
                    'Part_C\Resources\Roadmaps\Skill_Based_Roadmap\Photos\Python.png', use_column_width=True)
                pdf_helper(
                    'Part_C\Resources\Roadmaps\Skill_Based_Roadmap\Python.pdf', 'Python Learning Roadmap')

            with col26:
                st.image(
                    'Part_C\Resources\Roadmaps\Skill_Based_Roadmap\Photos\React.png', use_column_width=True)
                pdf_helper(
                    'Part_C\Resources\Roadmaps\Skill_Based_Roadmap\React.pdf', 'React Learning Roadmap')

        st.text("\n")
        st.text("\n")

        with st.container():
            col27, col28, col29, col30 = st.columns(4)

            with col27:
                st.image(image_helper(
                    'Part_C\Resources\Roadmaps\Skill_Based_Roadmap\Photos\Spring_boot.png'), use_column_width=True)
                pdf_helper('Part_C\Resources\Roadmaps\Skill_Based_Roadmap\Spring-boot.pdf',
                           'Spring Boot Learning Roadmap')

            with col28:
                st.image(image_helper(
                    'Part_C\Resources\Roadmaps\Skill_Based_Roadmap\Photos\System_Design.jpg'), use_column_width=True)
                pdf_helper(
                    'Part_C\Resources\Roadmaps\Skill_Based_Roadmap\System-design.pdf', 'System Design Roadmap')

            with col29:
                st.image(image_helper(
                    'Part_C\Resources\Roadmaps\Skill_Based_Roadmap\Photos\Typescript.png'), use_column_width=True)
                pdf_helper('Part_C\Resources\Roadmaps\Skill_Based_Roadmap\Typescript.pdf',
                           'Typescript Learning Roadmap')

            with col30:
                st.image(image_helper(
                    'Part_C\Resources\Roadmaps\Skill_Based_Roadmap\Photos\Vuejs.jpg'), use_column_width=True)
                pdf_helper(
                    'Part_C\Resources\Roadmaps\Skill_Based_Roadmap\Vue.pdf', 'VueJS Learning Roadmap')
