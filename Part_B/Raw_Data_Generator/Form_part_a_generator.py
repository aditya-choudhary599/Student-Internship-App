import random
import pandas as pd
import string

df = pd.read_csv(
    "~\Desktop\RPOOPS\Mini Project\Part_B\Raw_Data_Generator\Major Recruiters --2021-2022.csv")


def generate_company_name():
    list_of_names = df['Name of Company'].unique().tolist()
    ans = random.choice(list_of_names)
    # print(ans)
    return {'Name of company': ans}


def generate_company_address():
    list_of_address = df['Location'].unique().tolist()
    ans = random.choice(list_of_address)
    # print(ans)
    return {'Address of company': ans}


def generate_company_number():
    phone_num = '9' + ''.join([str(random.randint(0, 9))
                              for i in range(0, 9, 1)])
    # print(ans)
    return {'Phone Number': phone_num}


def generate_company_email_address(company_name: str):
    letters = string.ascii_lowercase
    username = company_name.lower().replace(' ', '')
    domain = 'internship' + '.com'
    email = username + '@' + domain
    # print(email)
    return {'Email Address': email}


def generate_company_previous_visited_to_coep():
    ans = random.choice(["Yes", "No"])
    # print(ans)
    return {'Previous Visited COEP': ans}


def generate_company_work_mode():
    ans = random.choice(["Work from Home", "Work from office"])
    # print(ans)
    return {'Work Mode': ans}


def generate_company_min_cgpa_criteria():
    ans = random.randint(60, 100)/10
    # print(ans)
    return {'Min CGPA': ans}


def generate_company_seats_for_boys():
    ans = random.randint(0, 10)
    # print(ans)
    return {'Seats for Boys': ans}


def generate_company_seats_for_girls():
    ans = random.randint(0, 10)
    # print(ans)
    return {'Seats for Girls': ans}


def generate_company_dead_backlogs_permitted():
    ans = random.randint(0, 2)
    # print(ans)
    return {'Number of Dead Backlogs permitted': ans}


def generate_company_active_backlogs_permitted():
    ans = random.randint(0, 2)
    # print(ans)
    return {'Number of Active Backlogs permitted': ans}


def generate_company_campus_visiting_month():
    ans = random.choice([
        "June", "July", "August", "September", "October", "Novermber", "December"])
    # print(ans)
    return {'Preffered month of visiting campus': ans}


def generate_part_a_response():
    response = {}

    response.update(generate_company_name())
    response.update(generate_company_address())
    response.update(generate_company_number())
    response.update(generate_company_email_address(response['Name of company']))
    response.update(generate_company_previous_visited_to_coep())
    response.update(generate_company_work_mode())
    response.update(generate_company_min_cgpa_criteria())
    response.update(generate_company_seats_for_boys())
    response.update(generate_company_seats_for_girls())
    response.update(generate_company_dead_backlogs_permitted())
    response.update(generate_company_active_backlogs_permitted())
    response.update(generate_company_campus_visiting_month())

    return response
