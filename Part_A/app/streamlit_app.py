import streamlit as st
import pyrebase
import json
import pandas as pd
from PIL import Image

key_dict = json.loads(st.secrets["textkey1"])
firebase = pyrebase.initialize_app(key_dict)
db = firebase.database()

st.set_page_config(
    page_title="INTERNSHIP FORM FOR SY'S",
    page_icon="🏫",
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
    "<h1 style='text-align: center;'><u>👋Welcome to the COEP Tech University Internship form</u></h1>", unsafe_allow_html=True)

st.header('🔗Brief about COEP : ')
col1, col2 = st.columns([2, 4])
with col1:
    st.image(Image.open('Part_A/Resources/coep.jpg'))
    pass
with col2:
    sub_container = col2.container()
    sub_container.write("College of Engineering, Pune (CoEP), chartered in 1854 is a nationally respected leader in technical education. The institute is distinguished by its commitment to finding solutions to the great predicaments of the day through advanced technology. The institute has a rich history and dedication to the pursuit of excellence. CoEP offers a unique learning experience across a spectrum of academic and social experiences. With a firm footing in truth and humanity, the institute gives you an understanding of both technical developments and the ethics that go with it. The curriculum is designed to enhance your academic experience through opportunities like internships, study abroad programmes and research facilities. The hallmark of CoEP education is its strong and widespread alumni network, support of the industry and the camaraderie that the institute shares with several foreign universities. The institute is consistently ranked amongst the top 20 technical colleges in India and its alumni have contributed a lion’s share in development of national infrastructure.")
    sub_container.markdown(
        "<a href='https://www.coep.org.in/'>Click here to get more info </a>", unsafe_allow_html=True)

st.divider()

st.title("🔗🧑‍💻Internship Form Part A")

company_data = {}

st.divider()

company_name = st.text_input(label='➡️**Name of Company:**')
if not company_name:
    st.warning('🛑Required Field')
    st.stop()
elif company_name.replace(' ', '').isalpha() == False:
    st.error('❌Invalid Name')
    st.stop()
else:
    st.success('✅Valid Name')
    company_data['Name of company'] = company_name

company_address = st.text_input(label='➡️**Company Address:**')
if not company_address:
    st.warning('🛑Required Field')
    st.stop()
else:
    st.success('✅Valid Address')
    company_data['Address of company'] = company_address

company_number = st.text_input(label='➡️**Company Number:**', max_chars=10)
st.caption(
    body='This number will be responsible for further contact with the company')
if not company_number:
    st.warning('🛑Required Field')
    st.stop()
elif company_number.isnumeric() == False or len(company_number) < 10:
    st.error('❌Invalid Number')
    st.stop()
else:
    st.success('✅Valid Number')
    company_data['Phone number'] = str(company_number)

comapny_email_address = st.text_input(
    label='➡️**Email Id concerned with Internship**')
if not comapny_email_address:
    st.warning('🛑Required Field')
    st.stop()
else:
    st.success('✅Valid Email Address')
    company_data['Email Address'] = comapny_email_address

company_previous_visited_to_coep = st.radio(
    label='➡️**Any previous recruitement from COEP:**', options=["Yes", "No"])
company_data['Previous Visited COEP'] = company_previous_visited_to_coep

if company_previous_visited_to_coep == "Yes":
    st.write("_Thank-you for coming back this year._")
else:
    st.write("_We are happy to have on board this year._")

company_work_mode = st.radio(
    label='➡️**Desired Work Mode:**', options=["Work from Home", "Work from Office"])
company_data['Work Mode'] = company_work_mode

company_min_cgpa_criteria = st.slider(
    label='➡️**Minimum cgpa for being elligible for company**', min_value=6.0, max_value=10.0, step=0.1)
company_data['Min CGPA'] = company_min_cgpa_criteria

company_seats_for_boys = st.slider(
    label='➡️**Internship seats offered for boys:**', min_value=0, max_value=10, step=1)
company_data['Seats for Boys'] = company_seats_for_boys

company_seats_for_girls = st.slider(
    label='➡️**Internship seats offered for girls:**', min_value=0, max_value=10, step=1)
company_data['Seats for Girls'] = company_seats_for_girls

company_dead_backlogs_permitted = st.number_input(
    label='➡️**Number of deads backlogs permitted:**', min_value=0, max_value=2, step=1)
company_data['Number of Dead Backlogs permitted'] = company_dead_backlogs_permitted

company_active_backlogs_permitted = st.number_input(
    label='➡️**Number of active backlogs permitted:**', min_value=0, max_value=2, step=1)
company_data['Number of Active Backlogs permitted'] = company_active_backlogs_permitted

company_campus_visiting_month = st.selectbox(label='➡️**When will company come to campus to hire students:**', options=[
    "June", "July", "August", "September", "October", "Novermber", "December"])
company_data['Preffered month of visiting campus'] = company_campus_visiting_month

sbt_btn_1 = st.button(label='Submit Part A', on_click=None, key=1)

if "helper_1" not in st.session_state:
    st.session_state.helper_1 = False

if sbt_btn_1 or st.session_state.helper_1:
    st.session_state.helper_1 = True
    st.success(
        'Your part A has been submitted sucessfuly. Please proceed to fill the B part of form.', icon="✅")

    st.divider()

    st.title("🔗🧑‍💻Internship Form Part B")

    st.divider()

    st.markdown("<h5 style='display:flex;'>Note : Here as per the domain selected by you need to do respective tech stack selection. Whichever fields are applicable to you fill that and let the remaining be empty. </h5>", unsafe_allow_html=True)

    company_skills_domains = st.radio(label="➡️**Select the domain for which you want to hire the students:**", options=[
                                      "🌐Web Development", "📱Mobile App Development", "📈Data Science and Analytics", "🧠Artificial Intelligence and Machine Learning", "☁️Cloud Engineer", "🔢Database Engineer", "👨‍💻Devops Engineer", "🕵🏻Cyber Security"])

    company_data['Domain to Hire'] = company_skills_domains

    if company_skills_domains == "🌐Web Development":
        st.divider()
        st.markdown(
            "<h2 style='text-align: center;'><b>🌐Web Development</b></h2>", unsafe_allow_html=True)
        col1, col2 = st.columns([2, 3])
        with col1:
            st.image(Image.open('Part_A/Resources/web_dev.jpg'),
                     use_column_width=True)

        web_dev_skillset = {}

        with col2:
            web_dev_frontend_languages = st.multiselect(
                label='➡️**Frontend Languages**', options=["HTML", "CSS", "Javascript"])
            web_dev_skillset['Frontent Languages'] = web_dev_frontend_languages

            web_dev_frontend_frameworks = st.multiselect(label='➡️**Frontend Frameworks**', options=[
                                                         "React.js", "Angular", "Vue.js", "Ember.js", "Backbone.js", "Bootstrap", "Materialize", "Foundation", "Bulma"])
            web_dev_skillset['Frontend Frameworks'] = web_dev_frontend_frameworks

            web_dev_backend_languages = st.multiselect(label='➡️**Backend Languages**', options=[
                                                       "JavaScript (Node.js)", "PHP", "Ruby", "Python", "Java", "Go", "C#"])
            web_dev_skillset['Backend Languages'] = web_dev_backend_languages

            web_dev_backend_frameworks = st.multiselect(label='➡️**Backend Frameworks**', options=[
                                                        "Express.js (Node.js)", "Django (Python)", "Ruby on Rails (Ruby)", "Laravel (PHP)", "Spring (Java)", "Flask (Python)", "ASP.NET (C#)", "Gin (Go)"])
            web_dev_skillset['Backend Frameworks'] = web_dev_backend_frameworks

            web_dev_database = st.multiselect(label='➡️**Databases for Websites**', options=[
                                              "MySQL", "PostgreSQL", "Oracle", "Microsoft SQL Server", "MongoDB", "Couchbase", "Cassandra", "Redis"])
            web_dev_skillset['Databases for Websites'] = web_dev_database

            web_dev_servers = st.multiselect(
                label='➡️**Website Servers**', options=["Apache", "Nginx", "IIS"])
            web_dev_skillset['Website Servers'] = web_dev_servers

            web_dev_deployment = st.multiselect(
                label='➡️**Website Deployment**', options=["Docker", "Kubernetes"])
            web_dev_skillset['Website Deployment'] = web_dev_deployment

            web_dev_testing = st.multiselect(label='➡️**Website Testing Tools**', options=[
                                             "Jest", "Mocha", "Jasmine", "Cypress", "Selenium"])
            web_dev_skillset['Website Testing Tools'] = web_dev_testing

            company_data['Skillsets requirements'] = web_dev_skillset

        st.divider()

    elif company_skills_domains == "📱Mobile App Development":
        st.divider()
        st.markdown(
            "<h2 style='text-align: center;'><b>📱Mobile App Development</b></h2>", unsafe_allow_html=True)
        col1, col2 = st.columns([2, 3])
        with col1:
            st.image(Image.open('Part_A/Resources/App_dev.jpeg'),
                     use_column_width=True)

        app_dev_skillset = {}

        with col2:
            app_dev_native_app = st.multiselect(
                label='➡️**Native Mobile App Development**', options=["Java (Android)", "Swift/Objective-C (iOS)"])
            app_dev_skillset['Native Mobile App Development'] = app_dev_native_app

            app_dev_cross_platform = st.multiselect(
                label='➡️**Cross-Platform Mobile App Development**', options=["React Native", "Xamarin", "Flutter"])
            app_dev_skillset['Cross-Platform Mobile App Development'] = app_dev_cross_platform

            app_dev_backend_languages = st.multiselect(label='➡️**Backend Development Languages**', options=[
                "JavaScript (Node.js)", "PHP", "Ruby", "Python", "Java", "Go", "C#"])
            app_dev_skillset['Backend Development Languages'] = app_dev_backend_languages

            app_dev_backend_frameworks = st.multiselect(label='➡️**Backend Development Frameworks**', options=[
                "Express.js (Node.js)", "Django (Python)", "Ruby on Rails (Ruby)", "Laravel (PHP)", "Spring (Java)", "Flask (Python)", "ASP.NET (C#)", "Gin (Go)"])
            app_dev_skillset['Backend Development Frameworks'] = app_dev_backend_frameworks

            app_dev_databases = st.multiselect(label='➡️**Databases for Apps**', options=[
                "MySQL", "PostgreSQL", "Oracle", "Microsoft SQL Server", "MongoDB", "Couchbase", "Cassandra", "Redis"])
            app_dev_skillset['Databases for Apps'] = app_dev_databases

            app_dev_web_services = st.multiselect(
                label='➡️**Web Services for App Development**', options=["RESTful APIs", "GraphQL"])
            app_dev_skillset['Web Services for App Development'] = app_dev_web_services

            app_dev_cloud_platforms = st.multiselect(
                label='➡️**Cloud Platform**', options=["AWS", "Google Cloud Platform", " Microsoft Azure"])
            app_dev_skillset['Cloud Platform'] = app_dev_cloud_platforms

            app_dev_deployment = st.multiselect(
                label='➡️**Deployment of App**', options=["Docker", "Kubernetes"])
            app_dev_skillset['Deployment of App'] = app_dev_deployment

            app_dev_testing = st.multiselect(label='➡️**Testing of App**', options=[
                                             "Jest", "Mocha", "Jasmine", " Appium", "Selenium", "Cypress"])
            app_dev_skillset['Testing of App'] = app_dev_testing

            company_data['Skillsets requirements'] = app_dev_testing

        st.divider()

    elif company_skills_domains == "📈Data Science and Analytics":
        st.divider()
        st.markdown(
            "<h2 style='text-align: center;'><b>📈Data Science and Analytics</b></h2>", unsafe_allow_html=True)
        col1, col2 = st.columns([2, 3])
        with col1:
            st.image(Image.open('Part_A/Resources/data.jpg'), use_column_width=True)

        data_sci_skillset = {}

        with col2:
            data_collection_and_storage = st.multiselect(
                label='➡️**Data Collection and Storage**', options="HDFS, MapReduce, YARN, Hive, HBase,Spark SQL, Spark Streaming, MLlib, GraphX,MongoDB, Cassandra, Redis".split(','))
            data_sci_skillset['Data Collection and Storage'] = data_collection_and_storage

            data_cleaning_and_processing = st.multiselect(
                label='➡️**Data Cleaning and Preprocessing**', options="Pandas, NumPy, Scikit-learn, Tidyverse, Dplyr, Data.table,OpenRefine".split(','))
            data_sci_skillset['Data Cleaning and Preprocessing'] = data_cleaning_and_processing

            data_visulazation = st.multiselect(
                label='➡️**Data Visualization**', options="Tableau,PowerBI,ggplot2 in R".split(','))
            data_sci_skillset['Data Visualization'] = data_visulazation

            data_statstical_analysis = st.multiselect(
                label='➡️**Statistical Analysis**', options="SAS,SPSS,Base R,Tidyverse,Data.table".split(','))
            data_sci_skillset['Statistical Analysis'] = data_statstical_analysis

            data_business_intelligence = st.multiselect(
                label='➡️**Business Intelligence (BI)**', options="SAP BusinessObjects,Oracle BI,IBM Cognos".split(','))
            data_sci_skillset['Business Intelligence (BI)'] = data_business_intelligence

            data_warehousing = st.multiselect(
                label='➡️**Data Warehousing**', options="Snowflake,Amazon Redshift,Microsoft SQL Server".split(','))
            data_sci_skillset['Data Warehousing'] = data_warehousing

            company_data['Skillsets requirements'] = data_sci_skillset

        st.divider()

    elif company_skills_domains == "🧠Artificial Intelligence and Machine Learning":
        st.divider()
        st.markdown(
            "<h2 style='text-align: center;'><b>🧠Artificial Intelligence and Machine Learning</b></h2>", unsafe_allow_html=True)
        col1, col2 = st.columns([2, 3])
        with col1:
            st.image(Image.open('Part_A/Resources/AIML.jpg'), use_column_width=True)

        aiml_skillset = {}

        with col2:
            aiml_nlp = st.multiselect(label='➡️**Natural Language Processing (NLP)**',
                                      options="Natural Language Toolkit (NLTK),Stanford NLP,Microsoft Cognitive Services,spaCy,AllenNLP,Google Cloud Natural Language API".split(','))
            aiml_skillset['Natural Language Processing (NLP)'] = aiml_nlp

            aiml_computer_vision = st.multiselect(
                label='➡️**Computer Vision**', options="OpenCV,TensorFlow,PyTorch,YOLO,Mask R-CNN,Detectron2".split(','))
            aiml_skillset['Computer Vision'] = aiml_computer_vision

            aiml_deep_learning = st.multiselect(
                label='➡️**Deep Learning**', options="TensorFlow,Keras,PyTorch,Caffe,MXNet,ONNX".split(','))
            aiml_skillset['Deep Learning'] = aiml_deep_learning

            aiml_machine_learning = st.multiselect(
                label='➡️**Machine Learning**', options="Scikit-learn,R,Weka,H2O.ai,XGBoost,RapidMiner".split(','))
            aiml_skillset['Machine Learning'] = aiml_machine_learning

            aiml_robotics = st.multiselect(
                label='➡️**Robotics**', options="Robot Operating System (ROS),Gazebo,PyBullet,TensorFlow Robotics,RoboFlow,ROS 2".split(','))
            aiml_skillset['Robotics'] = aiml_robotics

            company_data['Skillsets requirements'] = aiml_skillset

        st.divider()

    elif company_skills_domains == "☁️Cloud Engineer":
        st.divider()
        st.markdown(
            "<h2 style='text-align: center;'><b>☁️Cloud Engineer</b></h2>", unsafe_allow_html=True)
        col1, col2 = st.columns([2, 3])
        with col1:
            st.image(Image.open('Part_A/Resources/cloud.png'), use_column_width=True)

        cloud_skillset = {}

        with col2:
            cloud_infra_languages = st.multiselect(label='➡️**Cloud Infrastructure Programming languages**',
                                                   options="Terraform, CloudFormation, Azure Resource Manager Templates".split(','))
            cloud_skillset['Cloud Infrastructure Programming languages'] = cloud_infra_languages

            cloud_infra_frameworks = st.multiselect(
                label='➡️**Cloud Infrastructure Frameworks**', options=" AWS Cloud Development Kit (CDK), Pulumi".split(','))
            cloud_skillset['Cloud Infrastructure Frameworks'] = cloud_infra_frameworks

            cloud_storage_languages = st.multiselect(
                label='➡️**Cloud Storage Programming languages**', options=" Java, Python, Node.js, C#".split(','))
            cloud_skillset['Cloud Storage Programming languages'] = cloud_storage_languages

            cloud_storage_framewoks = st.multiselect(
                label='➡️**Cloud Storage Frameworks**', options="AWS SDK for Java, AWS SDK for Python, AWS SDK for .NET".split(','))
            cloud_skillset['Cloud Storage Frameworks'] = cloud_storage_framewoks

            cloud_computing_languages = st.multiselect(
                label='➡️**Cloud Computing Programming languages**', options="Python, Java, Node.js, Go, .NET".split(','))
            cloud_skillset['Cloud Computing Programming languages'] = cloud_computing_languages

            cloud_computing_frameworks = st.multiselect(
                label='➡️**Cloud Computing Frameworks**', options="AWS Lambda, Google Cloud Functions, Azure Functions".split(','))
            cloud_skillset['Cloud Computing Frameworks'] = cloud_computing_frameworks

            cloud_networking_languages = st.multiselect(
                label='➡️**Cloud Networking Programming languages**', options="Python, Java, C#, Go".split(','))
            cloud_skillset['Cloud Networking Programming languages'] = cloud_networking_languages

            cloud_networking_frameworks = st.multiselect(
                label='➡️**Cloud Networking Frameworks**', options="AWS Network Development Kit (NDK), Google Cloud Network Connectivity Center".split(','))
            cloud_skillset['Cloud Networking Frameworks'] = cloud_networking_frameworks

            cloud_security_languages = st.multiselect(
                label='➡️**Cloud Security Programming languages**', options="Python, Java, C#".split(','))
            cloud_skillset['Cloud Security Programming languages'] = cloud_security_languages

            cloud_security_frameworks = st.multiselect(
                label='➡️**Cloud Security Frameworks**', options="AWS Identity and Access Management (IAM), Azure Active Directory".split(','))
            cloud_skillset['Cloud Security Frameworks'] = cloud_security_frameworks

            cloud_monitoring_languages = st.multiselect(
                label='➡️**Cloud Monitoring Programming languages**', options=" Python, Java, Go".split(','))
            cloud_skillset['Cloud Monitoring Programming languages'] = cloud_monitoring_languages

            cloud_monitoring_frameworks = st.multiselect(
                label='➡️**Cloud Monitoring Frameworks**', options="AWS CloudWatch, Google Cloud Monitoring, Azure Monitor".split(','))
            cloud_skillset['Cloud Monitoring Frameworks'] = cloud_monitoring_frameworks

            company_data['Skillsets requirements'] = cloud_skillset

        st.divider()

    elif company_skills_domains == "🔢Database Engineer":
        st.divider()
        st.markdown(
            "<h2 style='text-align: center;'><b>🔢Database Engineer</b></h2>", unsafe_allow_html=True)
        col1, col2 = st.columns([2, 3])
        with col1:
            st.image(Image.open('Part_A/Resources/database.png'),
                     use_column_width=True)

        dbms_skillset = {}

        with col2:
            dbms_database_design = st.multiselect(
                '➡️**Database Design**', options="SQL, ER Diagrams".split(','))
            dbms_skillset['Database Design'] = dbms_database_design

            dbms_database_development = st.multiselect(
                '➡️**Datbase Development**', options="SQL, PL/SQL, T-SQL, Oracle Database, MySQL, PostgreSQL, SQL Server".split(','))
            dbms_skillset['Datbase Development'] = dbms_database_development

            dbms_administration = st.multiselect(
                label='➡️**Database Administration**', options="SQL, Oracle Database, MySQL, PostgreSQL, SQL Server".split(','))
            dbms_skillset['Database Administration'] = dbms_administration

            dbms_migration = st.multiselect(
                label='➡️**Database Migration**', options=" SQL, Python,AWS Database Migration Service, Oracle Data Integrator, Apache NiFi".split(','))
            dbms_skillset['Database Migration'] = dbms_migration

            dbms_tuning = st.multiselect(label='➡️**Database Performance Tuning**',
                                         options="SQL, PL/SQL, T-SQL,Oracle Enterprise Manager, SQL Server Management Studio, MySQL Workbench".split(','))
            dbms_skillset['Database Performance Tuning'] = dbms_tuning

            dbms_security = st.multiselect(
                label='➡️**Database Security**', options="SQL, PL/SQL, T-SQL, Oracle Database Vault, Microsoft SQL Server Audit, MySQL Enterprise Security".split(','))
            dbms_skillset['Database Security'] = dbms_security

            dbms_warehousing = st.multiselect(
                label='➡️**Data Warehousing**', options="SQL, PL/SQL, T-SQL,Oracle Warehouse Builder, SQL Server Integration Services, Pentaho Data Integration".split(','))
            dbms_skillset['Data Warehousing'] = dbms_warehousing

            dbms_big_data = st.multiselect(
                label='➡️**Big Data**', options="SQL, HiveQL, Pig Latin, Hadoop,Apache Hadoop, Apache Spark, Apache Hive, Apache Pig".split(','))
            dbms_skillset['Big Data'] = dbms_big_data

            company_data['Skillsets requirements'] = dbms_skillset

        st.divider()

    elif company_skills_domains == "👨‍💻Devops Engineer":
        st.divider()
        st.markdown(
            "<h2 style='text-align: center;'><b>👨‍💻Devops Engineer</b></h2>", unsafe_allow_html=True)
        col1, col2 = st.columns([2, 3])
        with col1:
            st.image(Image.open('Part_A/Resources/devops.jpg'),
                     use_column_width=True)

        devops_skillset = {}

        with col2:
            devops_version_control = st.multiselect(
                label='➡️**Version Control**', options="Git, GitHub, GitLab, Bitbucket".split(','))
            devops_skillset['Version Control'] = devops_version_control

            devops_continous_integration = st.multiselect(
                label='➡️**Continuous Integration**', options="Jenkins, Travis CI, CircleCI,Groovy, Java, Ruby, Python".split(','))
            devops_skillset['Continuous Integration'] = devops_continous_integration

            devops_config_management = st.multiselect(
                label='➡️**Configuration Management**', options="Ansible, Chef, Puppet,YAML, Ruby, Python".split(','))
            devops_skillset['Configuration Management'] = devops_config_management

            devops_containerization = st.multiselect(
                label='➡️**Containerization**', options="Docker, Kubernetes,Docker Compose, Helm".split(','))
            devops_skillset['Containerization'] = devops_containerization

            devops_continous_deployment = st.multiselect(
                label='➡️**Continuous Deployment**', options="Ansible, Chef, Puppet,YAML, Ruby, Python".split(','))
            devops_skillset['Continuous Deployment'] = devops_continous_deployment

            devops_monitoring_and_logging = st.multiselect(
                label='➡️**Monitoring and Logging**', options=" Nagios, Grafana, Prometheus, ELK stack,YAML, Ruby, Python, Java".split(','))
            devops_skillset['Monitoring and Logging'] = devops_monitoring_and_logging

            devops_collaboration_and_communication = st.multiselect(
                label='➡️**Collaboration and Communication**', options="Slack, Microsoft Teams, Jira, Trello".split(','))
            devops_skillset['Collaboration and Communication'] = devops_collaboration_and_communication

            company_data['Skillsets requirements'] = devops_skillset

        st.divider()

    elif company_skills_domains == "🕵🏻Cyber Security":
        st.divider()
        st.markdown(
            "<h2 style='text-align: center;'><b>🕵🏻Cyber Security</b></h2>", unsafe_allow_html=True)
        col1, col2 = st.columns([2, 3])
        with col1:
            st.image(Image.open('Part_A/Resources/cyber_security.jpg'),
                     use_column_width=True)

        cs_skillset = {}

        with col2:
            cs_network_security = st.multiselect(
                label='➡️**Network Security**', options="Cisco Security Solutions, Juniper Networks Security Solutions,Snort".split(','))
            cs_skillset['Network Security'] = cs_network_security

            cs_app_security = st.multiselect(
                label='➡️**Application Security**', options="Advanced Encryption Standard (AES), Data Encryption Standard (DES), Blowfish, RSA, MD5, SHA-1, SHA-2, SHA-3,LDAP, SAML, OAuth, OpenID Connect".split(','))
            cs_skillset['Application Security'] = cs_app_security

            cs_endpoint_security = st.multiselect(
                label='➡️**Endpoint Security**', options=" McAfee Endpoint Security, Symantec Endpoint Protection, Trend Micro Endpoint Security".split(','))
            cs_skillset['Endpoint Security'] = cs_endpoint_security

            cs_cloud_security = st.multiselect(
                label='➡️**Cloud Security**', options="Active Directory,Amazon Web Services (AWS) Security Tools, Microsoft Azure Security Tools, Google Cloud Platform (GCP) Security Tools".split(','))
            cs_skillset['Cloud Security'] = cs_cloud_security

            cs_data_security = st.multiselect(
                label='➡️**Data Security**', options="Advanced Encryption Standard (AES), Data Encryption Standard (DES), Blowfish, RSA, MD5, SHA-1, SHA-2, SHA-3".split(','))
            cs_skillset['Data Security'] = cs_data_security

            cs_web_security = st.multiselect(
                label='➡️**Web Application Security**', options="Metasploit Framework, Spring Framework,OWASP ZAP, Burp Suite, Acunetix, Nessus, Qualys, McAfee Secure, WebInspect, AppScan".split(','))
            cs_skillset['Web Application Security'] = cs_web_security

            company_data['Skillsets requirements'] = cs_skillset

        st.divider()

    sbt_btn_2 = st.button(label='Submit Form B', on_click=None)

    if sbt_btn_2:
        temp_dict=company_data['Skillsets requirements']
        del company_data['Skillsets requirements']
        for key in temp_dict:
            if len(temp_dict[key])==0:
                company_data[key]='N/A'
            else:
                company_data[key]=",".join(temp_dict[key])
        
        st.subheader('The data submitted by you is as follows')
        st.write(company_data)
        
        if (company_skills_domains == '🌐Web Development'):
            db.child("Web Development").push(company_data)
            st.success("✅Data written succesfully in database")

        elif (company_skills_domains == '📱Mobile App Development'):
            db.child("Mobile App Development").push(company_data)
            st.success("✅Data written succesfully in database")

        elif company_skills_domains == '📈Data Science and Analytics':
            db.child("Data Science and Analytics").push(company_data)
            st.success("✅Data written succesfully in database")

        elif company_skills_domains == '🧠Artificial Intelligence and Machine Learning':
            db.child("Artificial Intelligence and Machine Learning").push(company_data)
            st.success("✅Data written succesfully in database")

        elif company_skills_domains == '☁️Cloud Engineer':
            db.child("Cloud Enginner").push(company_data)
            st.success("✅Data written succesfully in database")

        elif company_skills_domains == '🔢Database Engineer':
            db.child("Database Engineer").push(company_data)
            st.success("✅Data written succesfully in database")

        elif company_skills_domains == '👨‍💻Devops Engineer':
            db.child("Devops Engineer").push(company_data)
            st.success("✅Data written succesfully in database")

        elif company_skills_domains == '🕵🏻Cyber Security':
            db.child("Cyber Security").push(company_data)
            st.write("✅Data written succesfully in database")
