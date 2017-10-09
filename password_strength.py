import getpass

#password = getpass.getpass('Password: ')
password = input('Password: ')


def get_password_strength(password):
    assessment = 0
    special_simbols = ['@','#','$','!','?']
    top_pass = [
    '123456',
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
    '1q2w3e']

    if len(password) < 6:
        assessment += 1
    elif len(password) < 9:
        assessment += 2
    elif len(password) < 11:
        assessment += 3
    elif len(password) < 13:
        assessment += 4
    else:
        assessment += 5

    low_letter = 0
    upper_letter = 0
    digit_count = 0
    special_simbols_count = 0
    same_letters_count = 0
    for letter in password:
        if 'a'<=letter<='z':
            low_letter += 1
        elif 'A'<=letter<='Z':
            upper_letter += 1
        elif '0'<=letter<='9':
            digit_count += 1
        elif special_simbols.count(letter)>0:
            special_simbols_count += 1
        if password.count(letter)>len(password)/2:
            same_letters_count += 1


    if (upper_letter!=0) and (low_letter!=0):
        assessment = assessment + 1

    if (digit_count != 0) and ((upper_letter != 0) and (low_letter != 0)):
        assessment = assessment + 1

    if  special_simbols_count != 0:
        assessment = assessment + 1
    if same_letters_count == 0:
        assessment += 1

    if top_pass.count(password) == 0:
        assessment = assessment + 1
    return assessment

if __name__ == '__main__':
    print('password assesment:',get_password_strength(password))
