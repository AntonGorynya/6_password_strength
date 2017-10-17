import getpass
import re
from collections import Counter


def check_len(password):
    assessment = 0
    if len(password) < 6:
        assessment += 1
    elif len(password) < 9:
        assessment += 2
    elif len(password) < 11:
        assessment += 3
    elif len(password) >= 13:
        assessment += 4
    return assessment


def check_top_password(password):
    assessment = 0
    top_pass = ['123456',
                '123456789',
                'qwerty',
                '12345678',
                '111111',
                '1234567890',
                '1234567',
                'password',
                'password1',
                '123123',
                '987654321',
                'qwertyuiop',
                'mynoob',
                '123321',
                '666666',
                '18atcskd2w',
                '7777777',
                '1q2w3e4r',
                '654321',
                '555555',
                '3rjs1la7qe',
                'google',
                '1q2w3e4r5t',
                '123qwe',
                'zxcvbnm',
                '1q2w3e'
                ]
    if top_pass.count(password) == 0:
        assessment +=  1
    return assessment


def check_symbols(password):
    assessment = 0
    special_simbols = {'@', '#', '$', '!', '?'}
    if (list(set(password)&special_simbols)) != []:
        assessment += 1
    if (Counter(password).most_common(1))[0][1] < len(password) / 2:
        assessment += 1
    if re.search(r'[a-z]', password) and re.search(r'[A-Z]', password):
        assessment += 1
    if (re.search(r'[a-z]', password) or re.search(r'[A-Z]', password)) and re.search(r'[0-9]', password):
        assessment += 1
    return assessment


def check_data_in_password(password, user_data):
    birthday = ''.join(re.findall(r'[0-9]+',user_data))
    print(birthday)
    if password.find(birthday) >= 0:
        return 0
    else:
        return 1


def get_password_strength(password, user_data):
    assessment = 0
    assessment = check_len(password) + assessment
    assessment = check_symbols(password) + assessment
    assessment = check_top_password(password) + assessment
    assessment = check_data_in_password(password, user_data) + assessment
    return assessment

if __name__ == '__main__':
    birthday = input("input your birthday((in DD-MM-YYYY format)): ")
    password = input('Password: ')
    print('password assesment:', get_password_strength(password, birthday))
