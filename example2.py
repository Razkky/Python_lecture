# Project on While loop

# Example 2

# num = 100

# while num > 0:
#     print(num)
#     num = num - 1

# print('Finished')

# Example 3

# correct_answer = 7
# number_attempt = 0
# number_chances = 3
# while number_attempt < number_chances:
#     guess = input("Guess a random number: ")
#     try:
#         guess = int(guess)
#         if guess == correct_answer:
#             print('Congratulations you guessed right')
#             break
#         else:
#             number_attempt = number_attempt + 1
#             print("Wrong guess Try again")
#     except ValueError:
#         print('Enter a valid number')

# if number_attempt == 3:
#     print('Maximum number of attempts reached')


# password = 'aminah.aliyah'

# while True :
#     user_password = input('Enter your password: ')
#     if user_password == password:
#         print('Correct Password')
#         print('Access Granted')
#         break
#     else:
#         print('Incorrect Password')
#         print('Access Denied')
#         print('Try Again')
#         continue
    
print('printing for loop')
for i in range(1, 11):
    print(i)
    # if i == 5:
    #     break

print()

print('printing while loop')
i  = 1

while i < 11:
    print(i)
    i = i + 1
