#Write a program that outputs the numbers from 1 to 100. All numbers that are divisible by three should be replaced by Fizz and all numbers that are divisible by 5 should be replaced by Buzz. Numbers that are divisible by both 3 and 5 will be replaced by "FizzBuzz".
#Note: You can check the divisibility with the modulo operator ``%`. The output of the function should look like this:

for number in range(1,101,1):
#    print(number)
    if number % 3 == 0 and number % 5==0:
        print("FizzBuzz")
    elif number % 3 == 0 and not number % 5==5:
        print("Fizz")
    else:
        print(number)
