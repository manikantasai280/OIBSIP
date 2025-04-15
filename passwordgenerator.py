import random
import string
password_length=int(input("enter password length"))
if(password_length<4):
    print("password too short")
else:
        lowercase_letters_length=int(input("enter how many lower case letters include in password"))
        uppercase_letters_length=int(input("enter how many upper case letters include in password"))
        numbers_length=int(input("enter how many numbers include in password"))
        special_char_length=int(input("enter how many special charachters include in password"))
        length=lowercase_letters_length+uppercase_letters_length+numbers_length+special_char_length
        if(length!=password_length):
            print("Please cross-verify: total character counts don't match the desired password length.")
        else:
            lowercase_letters=random.choices(string.ascii_lowercase,k=lowercase_letters_length)
            uppercase_letters=random.choices(string.ascii_uppercase,k=uppercase_letters_length)
            numbers=random.choices(string.digits,k=numbers_length)
            special_charachters=random.choices(string.punctuation,k=special_char_length)
            charachters=lowercase_letters+uppercase_letters+numbers+special_charachters
            random.shuffle(charachters)
            password=''.join(charachters)
            print("your password is :" + password)