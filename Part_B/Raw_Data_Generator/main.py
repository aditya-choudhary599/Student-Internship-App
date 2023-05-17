import sys
sys.path.append('Part_B\Raw_Data_Generator')

from Form_part_a_generator import *
from Form_part_b_generator import *

import pandas as pd

# -----GENERATING RAW WEB DEV DATA-----
dataset=[]
x=random.randint(40,75)
for i in range(0,x,1):
    temp=generate_part_a_response()
    temp.update(generate_web_dev_response())
    dataset.append(temp)

df=pd.DataFrame(dataset)
df.to_csv('~\Desktop\RPOOPS\Mini Project\Part_B\Raw_Data_Generated\Raw_web_dev_data.csv')


# -----GENERATING RAW APP DEV DATA-----
dataset=[]
x=random.randint(40,75)
for i in range(0,x,1):
    temp=generate_part_a_response()
    temp.update(generate_app_dev_response())
    dataset.append(temp)

df=pd.DataFrame(dataset)
df.to_csv('~\Desktop\RPOOPS\Mini Project\Part_B\Raw_Data_Generated\Raw_app_dev_data.csv')

# -----GENERATING RAW DATA SCI DATA-----
dataset=[]
x=random.randint(40,75)
for i in range(0,x,1):
    temp=generate_part_a_response()
    temp.update(generate_data_sci_response())
    dataset.append(temp)

df=pd.DataFrame(dataset)
df.to_csv('~\Desktop\RPOOPS\Mini Project\Part_B\Raw_Data_Generated\Raw_data_sci_data.csv')

# -----GENERATING RAW AIML DATA-----
dataset=[]
x=random.randint(40,75)
for i in range(0,x,1):
    temp=generate_part_a_response()
    temp.update(generate_aiml_response())
    dataset.append(temp)

df=pd.DataFrame(dataset)
df.to_csv('~\Desktop\RPOOPS\Mini Project\Part_B\Raw_Data_Generated\Raw_aiml_data.csv')

# -----GENERATING RAW CLOUD DATA-----
dataset=[]
x=random.randint(40,75)
for i in range(0,x,1):
    temp=generate_part_a_response()
    temp.update(generate_cloud_response())
    dataset.append(temp)

df=pd.DataFrame(dataset)
df.to_csv('~\Desktop\RPOOPS\Mini Project\Part_B\Raw_Data_Generated\Raw_cloud_data.csv')

# -----GENERATING RAW DBMS DATA-----
dataset=[]
x=random.randint(40,75)
for i in range(0,x,1):
    temp=generate_part_a_response()
    temp.update(generate_dbms_response())
    dataset.append(temp)

df=pd.DataFrame(dataset)
df.to_csv('~\Desktop\RPOOPS\Mini Project\Part_B\Raw_Data_Generated\Raw_dbms_data.csv')

# -----GENERATING RAW DEVOPS DATA-----
dataset=[]
x=random.randint(40,75)
for i in range(0,x,1):
    temp=generate_part_a_response()
    temp.update(generate_devops_response())
    dataset.append(temp)

df=pd.DataFrame(dataset)
df.to_csv('~\Desktop\RPOOPS\Mini Project\Part_B\Raw_Data_Generated\Raw_devops_data.csv')

# -----GENERATING RAW CS DATA-----
dataset=[]
x=random.randint(40,75)
for i in range(0,x,1):
    temp=generate_part_a_response()
    temp.update(generate_cs_response())
    dataset.append(temp)

df=pd.DataFrame(dataset)
df.to_csv('~\Desktop\RPOOPS\Mini Project\Part_B\Raw_Data_Generated\Raw_cs_data.csv')
