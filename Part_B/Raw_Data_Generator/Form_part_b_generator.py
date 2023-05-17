import random


def helper(options: list[str]) -> str:
    # here using sample function instead of choicesto generate unique random values
    ans = random.sample(options, k=random.randint(0, len(options)))
    for i in range(0, len(ans), 1):
        ans[i] = ans[i].strip()  # to remove the extra trailing spaces.
    if len(ans) == 0:
        return 'N/A'
    else:
        return ','.join(ans)


def generate_web_dev_response():
    web_dev_response = {}

    web_dev_response['Domain to Hire'] = "🌐Web Development"

    web_dev_response['Frontent Languages'] = helper(
        ["HTML", "CSS", "Javascript"])

    web_dev_response['Frontend Frameworks'] = helper([
        "React.js", "Angular", "Vue.js", "Ember.js", "Backbone.js", "Bootstrap", "Materialize", "Foundation", "Bulma"])

    web_dev_response['Backend Languages'] = helper([
        "JavaScript (Node.js)", "PHP", "Ruby", "Python", "Java", "Go", "C#"])

    web_dev_response['Backend Frameworks'] = helper([
        "Express.js (Node.js)", "Django (Python)", "Ruby on Rails (Ruby)", "Laravel (PHP)", "Spring (Java)", "Flask (Python)", "ASP.NET (C#)", "Gin (Go)"])

    web_dev_response['Databases for Websites'] = helper(
        ["MySQL", "PostgreSQL", "Oracle", "Microsoft SQL Server", "MongoDB", "Couchbase", "Cassandra", "Redis"])

    web_dev_response['Website Servers'] = helper(["Apache", "Nginx", "IIS"])

    web_dev_response['Website Deployment'] = helper(["Docker", "Kubernetes"])

    web_dev_response['Website Testing Tools'] = helper(
        ["Jest", "Mocha", "Jasmine", "Cypress", "Selenium"])

    return web_dev_response


def generate_app_dev_response():
    app_dev_response = {}

    app_dev_response['Domain to Hire'] = "📱Mobile App Development"

    app_dev_response['Native Mobile App Development'] = helper(
        ["Java (Android)", "Swift/Objective-C (iOS)"])

    app_dev_response['Cross-Platform Mobile App Development'] = helper(
        ["React Native", "Xamarin", "Flutter"])

    app_dev_response['Backend Development Languages'] = helper(
        ["JavaScript (Node.js)", "PHP", "Ruby", "Python", "Java", "Go", "C#"])

    app_dev_response['Backend Development Frameworks'] = helper(
        ["Express.js (Node.js)", "Django (Python)", "Ruby on Rails (Ruby)", "Laravel (PHP)", "Spring (Java)", "Flask (Python)", "ASP.NET (C#)", "Gin (Go)"])

    app_dev_response['Databases for Apps'] = helper(
        ["MySQL", "PostgreSQL", "Oracle", "Microsoft SQL Server", "MongoDB", "Couchbase", "Cassandra", "Redis"])

    app_dev_response['Web Services for App Development'] = helper(
        ["RESTful APIs", "GraphQL"])

    app_dev_response['Cloud Platform'] = helper(
        ["AWS", "Google Cloud Platform", " Microsoft Azure"])

    app_dev_response['Deployment of App'] = helper(["Docker", "Kubernetes"])

    app_dev_response['Testing of App'] = helper(
        ["Jest", "Mocha", "Jasmine", " Appium", "Selenium", "Cypress"])

    return app_dev_response


def generate_data_sci_response():
    data_sci_response = {}

    data_sci_response['Domain to Hire'] = "📈Data Science and Analytics"

    data_sci_response['Data Collection and Storage'] = helper(
        "HDFS, MapReduce, YARN, Hive, HBase,Spark SQL, Spark Streaming, MLlib, GraphX,MongoDB, Cassandra, Redis".split(','))

    data_sci_response['Data Cleaning and Preprocessing'] = helper(
        "Pandas, NumPy, Scikit-learn, Tidyverse, Dplyr, Data.table,OpenRefine".split(','))

    data_sci_response['Data Visualization'] = helper(
        "Tableau,PowerBI,ggplot2 in R".split(','))

    data_sci_response['Statistical Analysis'] = helper(
        "SAS,SPSS,Base R,Tidyverse,Data.table".split(','))

    data_sci_response['Business Intelligence (BI)'] = helper(
        "SAP BusinessObjects,Oracle BI,IBM Cognos".split(','))

    data_sci_response['Data Warehousing'] = helper(
        "Snowflake,Amazon Redshift,Microsoft SQL Server".split(','))

    return data_sci_response


def generate_aiml_response():
    aiml_response = {}

    aiml_response['Domain to Hire'] = "🧠Artificial Intelligence and Machine Learning"

    aiml_response['Natural Language Processing (NLP)'] = helper(
        "Natural Language Toolkit (NLTK),Stanford NLP,Microsoft Cognitive Services,spaCy,AllenNLP,Google Cloud Natural Language API".split(','))

    aiml_response['Computer Vision'] = helper(
        "OpenCV,TensorFlow,PyTorch,YOLO,Mask R-CNN,Detectron2".split(','))

    aiml_response['Deep Learning'] = helper(
        "TensorFlow,Keras,PyTorch,Caffe,MXNet,ONNX".split(','))

    aiml_response['Machine Learning'] = helper(
        "Scikit-learn,R,Weka,H2O.ai,XGBoost,RapidMiner".split(','))

    aiml_response['Robotics'] = helper(
        "Robot Operating System (ROS),Gazebo,PyBullet,TensorFlow Robotics,RoboFlow,ROS 2".split(','))

    return aiml_response


def generate_cloud_response():
    cloud_response = {}

    cloud_response['Domain to Hire'] = "☁️Cloud Engineer"

    cloud_response['Cloud Infrastructure Programming languages'] = helper(
        "Terraform, CloudFormation, Azure Resource Manager Templates".split(','))

    cloud_response['Cloud Infrastructure Frameworks'] = helper(
        " AWS Cloud Development Kit (CDK), Pulumi".split(','))

    cloud_response['Cloud Storage Programming languages'] = helper(
        " Java, Python, Node.js, C#".split(','))

    cloud_response['Cloud Storage Frameworks'] = helper(
        "AWS SDK for Java, AWS SDK for Python, AWS SDK for .NET".split(','))

    cloud_response['Cloud Computing Programming languages'] = helper(
        "Python, Java, Node.js, Go, .NET".split(','))

    cloud_response['Cloud Computing Frameworks'] = helper(
        "AWS Network Development Kit (NDK), Google Cloud Network Connectivity Center".split(','))

    cloud_response['Cloud Security Programming languages'] = helper(
        "Python, Java, C#".split(','))

    cloud_response['Cloud Security Frameworks'] = helper(
        "AWS Identity and Access Management (IAM), Azure Active Directory".split(','))

    cloud_response['Cloud Monitoring Programming languages'] = helper(
        " Python, Java, Go".split(','))

    cloud_response['Cloud Monitoring Frameworks'] = helper(
        "AWS CloudWatch, Google Cloud Monitoring, Azure Monitor".split(','))

    return cloud_response


def generate_dbms_response():
    dbms_response = {}

    dbms_response['Domain to Hire'] = "🔢Database Engineer"

    dbms_response['Database Design'] = helper("SQL, ER Diagrams".split(','))

    dbms_response['Datbase Development'] = helper(
        "SQL, PL/SQL, T-SQL, Oracle Database, MySQL, PostgreSQL, SQL Server".split(','))

    dbms_response['Database Administration'] = helper(
        "SQL, Oracle Database, MySQL, PostgreSQL, SQL Server".split(','))

    dbms_response['Database Migration'] = helper(
        " SQL, Python,AWS Database Migration Service, Oracle Data Integrator, Apache NiFi".split(','))

    dbms_response['Database Performance Tuning'] = helper(
        "SQL, PL/SQL, T-SQL,Oracle Enterprise Manager, SQL Server Management Studio, MySQL Workbench".split(','))

    dbms_response['Database Security'] = helper(
        "SQL, PL/SQL, T-SQL, Oracle Database Vault, Microsoft SQL Server Audit, MySQL Enterprise Security".split(','))

    dbms_response['Data Warehousing'] = helper(
        "SQL, PL/SQL, T-SQL,Oracle Warehouse Builder, SQL Server Integration Services, Pentaho Data Integration".split(','))

    dbms_response['Big Data'] = helper(
        "SQL, HiveQL, Pig Latin, Hadoop,Apache Hadoop, Apache Spark, Apache Hive, Apache Pig".split(','))

    return dbms_response


def generate_devops_response():
    devops_response = {}

    devops_response['Domain to Hire'] = "👨‍💻Devops Engineer"

    devops_response['Version Control'] = helper(
        "Git, GitHub, GitLab, Bitbucket".split(','))

    devops_response['Continuous Integration'] = helper(
        "Jenkins, Travis CI, CircleCI,Groovy, Java, Ruby, Python".split(','))

    devops_response['Configuration Management'] = helper(
        "Ansible, Chef, Puppet,YAML, Ruby, Python".split(','))

    devops_response['Containerization'] = helper(
        "Docker, Kubernetes,Docker Compose, Helm".split(','))

    devops_response['Continuous Deployment'] = helper(
        "Ansible, Chef, Puppet,YAML, Ruby, Python".split(','))

    devops_response['Monitoring and Logging'] = helper(
        " Nagios, Grafana, Prometheus, ELK stack,YAML, Ruby, Python, Java".split(','))

    devops_response['Collaboration and Communication'] = helper(
        "Slack, Microsoft Teams, Jira, Trello".split(','))

    return devops_response


def generate_cs_response():
    cs_response = {}

    cs_response['Domain to Hire'] = "🕵🏻Cyber Security"

    cs_response['Network Security'] = helper(
        "Cisco Security Solutions, Juniper Networks Security Solutions,Snort".split(','))

    cs_response['Application Security'] = helper(
        "Advanced Encryption Standard (AES), Data Encryption Standard (DES), Blowfish, RSA, MD5, SHA-1, SHA-2, SHA-3,LDAP, SAML, OAuth, OpenID Connect".split(','))

    cs_response['Endpoint Security'] = helper(
        " McAfee Endpoint Security, Symantec Endpoint Protection, Trend Micro Endpoint Security".split(','))

    cs_response['Cloud Security'] = helper(
        "Active Directory,Amazon Web Services (AWS) Security Tools, Microsoft Azure Security Tools, Google Cloud Platform (GCP) Security Tools".split(','))

    cs_response['Data Security'] = helper(
        "Advanced Encryption Standard (AES), Data Encryption Standard (DES), Blowfish, RSA, MD5, SHA-1, SHA-2, SHA-3".split(','))

    cs_response['Web Application Security'] = helper(
        "Metasploit Framework, Spring Framework,OWASP ZAP, Burp Suite, Acunetix, Nessus, Qualys, McAfee Secure, WebInspect, AppScan".split(','))

    return cs_response
