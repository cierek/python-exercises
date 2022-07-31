# Program that asks the user to enter three integer numbers. The program should output the largest of the three numbers

# Please enter the first number: 23
# Please enter the second number: 42
# Please enter the third number: 11

# The largest number is 42

number_one = int(input("Please enter a number one: "))
number_two = int(input("Please enter a number two: "))
number_three = int(input("Please enter a number three: "))
#print(number_one,number_two,number_three)

if number_one > number_two:
#    print("The largest number is", number_one)
    result = number_one
#    print(number_one)
elif number_two > number_three:
#    print("The largest number is", number_two)
#    print(number_two)
    result = number_two
else:
#    print("The largest number is",number_three)
#   print(number_three)
    result = number_three

print("The largest number is", result)
