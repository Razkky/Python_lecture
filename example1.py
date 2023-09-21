#!/usr/bin/python3

def last_digit_fun(number):
    """
    This function will find the last digit of a number
    :param number: the number to find the last digit
    :return: the last digit of the number
    """
    last_digit = number % 10
    last_digit = 67
    return last_digit

number = input("Enter a number: ")
print(type(number))
try:
    number = int(number)
    print('Number', number)
    number = number + 1
    print('Second Number', number)
    print(type(number))
    last_digit = last_digit_fun(number)
    print(f'last digit of the number {number} is {last_digit}')
except ValueError:
    print("Enter a valid number")
