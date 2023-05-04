from os import system
# from art import logo


def add(user_input_num1,user_input_num2):
    return user_input_num1 + user_input_num2

def sub(user_input_num1,user_input_num2):
    return user_input_num1 - user_input_num2

def mul(user_input_num1,user_input_num2):
    return user_input_num1 * user_input_num2

def div(user_input_num1,user_input_num2):
    return user_input_num1 / user_input_num2


'''*********************************************************************'''

user_input_num1 = int(input('Type your 1st Num:\n'))
system('cls')
user_input_mode = str(input('Type mode of Calculation: [a-add ,m-mul, s-sub, d-div]\n'))
system('cls')
user_input_num2 = int(input('Type your 2st Num:\n'))
system('cls')

#Calling Cal Func.
if user_input_mode == 'a':
    cal = add(user_input_num1,user_input_num2)

if user_input_mode == 'm':
    cal = mul(user_input_num1,user_input_num2)

if user_input_mode == 's':
    cal = sub(user_input_num1,user_input_num2)

if user_input_mode == 'd':
    cal = div(user_input_num1,user_input_num2)

#Giving Output
print(cal)
