# Lee Haynes
# Phone: + 44 (0) 785 374 0636
# Email: LeeHaynes2019@yandex.com
# Website: http://www.devcoder.me.uk/
# Instagram: junior_web_developer_2020


# Create password generator
import random

min_passwd_length = 8


# Created a password list
password_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!'_+=\"|\"{}:@;'<>,.?/'"


# Asking user to input a number
number_characters = int(
    input("Enter the total number of characters for you password "))
password_output = ""


# Here is the loop to serch and pick X number of charaters from the password list
for letters in range(number_characters):
    password_output += random.choice(password_list)
print(password_output)


# Here is a password length check
# If the password is less than 8 then the user will get a prompt asking if they are happy with there password choice if so great if not then a new password will be created
if (number_characters < min_passwd_length):
    print("This is not a good password length, I advise you to increase password length")
    confirm = input("Are you sure that your happy with the password?")
    if confirm == "Yes":
        for letters in range(number_characters):
            password_output += random.choice(password_list)
        print(password_output)
    elif confirm == "no" or confirm == "n":
        print("A stronger password has been chosen for you at random")
        for letters in range(number_characters+5):
            password_output += random.choice(password_list)

    # Here the password is printed to the screen.
    print(password_output)
