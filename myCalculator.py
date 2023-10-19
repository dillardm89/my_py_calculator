import time, sys, re

def numbers_list(user_input):
    numbers = re.findall(r'\d*\.*\d+', user_input)
    numbers = list(map(float, numbers))
    return numbers

def return_to_menu():
    input('Press "Enter" key to return to menu.')
    menu()

def add():
    user_input = input('Enter addition statement: ')
    input_error = re.findall(r'[-/*%=]', user_input)

    while input_error:
        print('Please enter only "+" operations.')
        input_error = ""
        user_input = input('Enter addition statement: ')

    if not input_error:
        numbers = numbers_list(user_input)

        numbers_add = numbers[0]
        for i in range(1,len(numbers)):
            numbers_add += numbers[i]

        print(numbers_add)
        return_to_menu()

def subtract():
    user_input = input('Enter subtraction statement: ')
    input_error = re.findall(r'[+/*%=]', user_input)

    while input_error:
        print('Please enter only "-" operations.')
        input_error = ""
        user_input = input('Enter subtraction statement: ')

    if not input_error:
        numbers = numbers_list(user_input)

        numbers_subtract = numbers[0]
        for i in range(1,len(numbers)):
            numbers_subtract -= numbers[i]

        print(numbers_subtract)
        return_to_menu()

def multiply():
    user_input = input('Enter multiplication statement: ')
    input_error = re.findall(r'([*]{2})|[-+/%=]', user_input)

    while input_error:
        print('Please enter only "*" operations.')
        input_error = ""
        user_input = input('Enter multiplication statement: ')

    if not input_error:
        numbers = numbers_list(user_input)


        numbers_multiply = numbers[0]
        for i in range(1, len(numbers)):
            numbers_multiply *= numbers[i]

        print(numbers_multiply)
        return_to_menu()


def divide():
    user_input = input('Enter division statement: ')
    input_error = re.findall(r'([/]{2})|[-+*%=]', user_input)

    while input_error:
        print('Please enter only "/" operations.')
        input_error = ""
        user_input = input('Enter division statement: ')

    if not input_error:
        numbers = numbers_list(user_input)

        numbers_divide = numbers[0]
        for i in range(1, len(numbers)):
            numbers_divide /= numbers[i]

        print(numbers_divide)
        return_to_menu()

def exitCalculator():
    print('Exiting...')
    time.sleep(2)
    sys.exit()

def menu ():
    print('Calculator Operations:\n1: Add\n2: Subtract\n3: Multiply\n4: Divide\n5: Exit')

    selection = int(input('Enter the operation number: '))

    if selection == 1:
        add()
    elif selection == 2:
        subtract()
    elif selection == 3:
        multiply()
    elif selection == 4:
        divide()
    else:
        exitCalculator()

if __name__ == "__main__":
    menu()
