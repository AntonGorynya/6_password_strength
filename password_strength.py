import getpass
import re
from collections import Counter
from string import punctuation


def get_len_assessment(password):
    assessment = 0
    short_len = 6
    medium_len = 9
    long_len = 11
    very_long_len = 13
    if len(password) < short_len:
        assessment += 1
    elif len(password) < medium_len:
        assessment += 2
    elif len(password) < long_len:
        assessment += 3
    elif len(password) >= very_long_len:
        assessment += 4
    return assessment


def load_forbiden_pass(path_to_file):
    with open(path_to_file) as forbiden_pass_file:
        forbiden_pass = forbiden_pass_file.readlines()
    return forbiden_pass


def check_forbiden_pass(password, forbiden_pass):
    return password not in forbiden_pass


def symbols_assessment(password):
    frequent_characters = 1
    assessment = 0
    if set(password).intersection(punctuation) != set():
        assessment += 1
    if (Counter(password).most_common(frequent_characters))[0][1] \
            < len(password) / 2:
        assessment += 1
    if re.search(r'[a-z]', password) and re.search(r'[A-Z]', password):
        assessment += 1
    if (re.search(r'[a-z]', password) or re.search(r'[A-Z]', password)) \
            and re.search(r'[0-9]', password):
        assessment += 1
    return assessment


def check_user_data_not_in_password(password, user_data):
    birthday = ''.join(re.findall(r'[0-9]+', user_data['birthday']))
    return password.find(birthday) < 0 and \
        password.find(user_data['company_name']) < 0


def get_password_strength(password, user_data, forbiden_pass):
    assessment = get_len_assessment(password) + symbols_assessment(password) \
                 + check_forbiden_pass(password, forbiden_pass) \
                 + check_user_data_not_in_password(password, user_data)
    return assessment

if __name__ == '__main__':
    birthday = input("input your birthday((in DD-MM-YYYY format)): ")
    company_name = input("input your company_name: ")
    user_data = {'birthday': birthday, 'company_name': company_name}
    password = getpass.getpass(prompt='Password: ')
    forbiden_pass = load_forbiden_pass('./forbiden_password.txt')
    print('password assesment:',
          get_password_strength(password, user_data, forbiden_pass))
