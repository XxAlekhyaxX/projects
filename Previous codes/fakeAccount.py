import random
from datetime import date

accounts = []

def generate_username_and_mail(name: str):
    clean_name = name.replace(" ", "").lower()
    rand_num = random.randint(10, 99)
    username = f"{clean_name}{rand_num}"
    mail = f"{clean_name}{rand_num}@gmail.com"
    return username, mail

def generate_dob() -> str:
    day = random.randint(1, 28)
    month = random.randint(1, 12)
    year = int(str(date.today())[:4])
    end_year = year - 19
    start_year = year - 30
    rand_year = random.randint(start_year, end_year)
    return f"{day}/{month}/{year}"

def generate_password(name: str) -> str:
    clean_name = name.replace(" ", "").lower()
    special_char = random.choice(['-', '_', '@', '#'])
    rand_num = random.randint(1000, 9999)
    return f"{clean_name}{special_char}{rand_num}"

def create_account(name: str, gender: str = "male"):
    username, mail = generate_username_and_mail(name)
    dob = generate_dob()
    password = generate_password(name)
    account = {
        "username": username,
        "name": name,
        "dob": dob,
        "mail": mail,
        "gender": gender,
        "password": password
    }
    accounts.append(account)
    return account
