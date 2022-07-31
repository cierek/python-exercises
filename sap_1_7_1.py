#A quadratic equation is an equation that can be written as
#ax^2 +bx +c = 0

#In this equation x represents an unknown number, and a, b, and c are representing known numbers. Possible solutions for a given quadratic equation can be calculated by the formula
#x = (-b +/-)

#The expression formula discriminant is called the discriminant. Using the discriminant makes it is easy to check the number of solutions for a given quadratic equation:

#If the discriminant is 0, the quadratic equation has exactly one real solution.
#If the discriminant is > 0, the quadratic equation has two real solutions.
#If the discriminant is < 0, the quadratic equation has two complex solutions.
#Write a program that asks the user for the numbers a, b and c. The program should then print out how many solutions the quadratic equation has.

a = int(input("Please enter the value of a:"))
b = int(input("Please enter the value of b:"))
c = int(input("Please enter the value of c:"))

delta = b*b -4*(a*c)
# print(delta)

if delta > 2:
    print("The quadratic equation has 2 real solutions.")
elif delta == 0:
    print("The quadratic equation has 1 real solution.")
else:
    print("The quadratic equation has 2 complex solutions.")
