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


def check_no_popular(password):
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
    if password not in top_pass:
        return True
    else:
        return False


def symbols_assessment(password):
    frequent_characters = 1
    assessment = 0
    if set(password).intersection(set(punctuation)) != {}:
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


def check_data_in_not_password(password, user_data):
    birthday = ''.join(re.findall(r'[0-9]+', user_data['birthday']))
    if password.find(birthday) >= 0 \
            and password.find(user_data['company_name']) >= 0:
        return False
    else:
        return True


def get_password_strength(password, user_data):
    assessment = get_len_assessment(password) + symbols_assessment(password) \
                 + check_no_popular(password) \
                 + check_data_in_not_password(password, user_data)
    return assessment

if __name__ == '__main__':
    birthday = input("input your birthday((in DD-MM-YYYY format)): ")
    company_name = input("input your company_name: ")
    user_data = {'birthday': birthday, 'company_name': company_name}
    password = getpass.getpass(prompt='Password: ')
    print('password assesment:', get_password_strength(password, user_data))
