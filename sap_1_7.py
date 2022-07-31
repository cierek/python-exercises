#Triangles can be classified based on their angles.

#A right triangle has one angle of 90°
#A obtuse triangle has one angle of more than 90°
#A triangle is acute if all three angles are less than 90°
#Write a program that asks the user for the values of three angles in degrees. First check if the entered values are valid. The values are only valid if they are >0 and if their sum is 180°. If the entered values are valid, classify the triangle as right, acute or obtuse.

#Below are two example executions of the program with invalid values:

#Please enter the first angle: 60
#Please enter the second angle: 60
#Please enter the third angle: 100
#The entered values are not valid.

#Please enter the first angle: 200
#Please enter the second angle: -10
#Please enter the third angle: -10
#Angles smaller than 0 are not valid.
#Here is another example execution of the program:

#Please enter the first angle: 60
#Please enter the second angle: 30
#Please enter the third angle: 90
#The triangle is a right triangle.

angle_one = input("Please enter the first angle:")
angle_two = input("Please enter the second angle:")
angle_three = input("Please enter the third angle:")

if (angle_one.isdigit() and angle_two.isdigit() and angle_three.isdigit()):
    angle_one = int(angle_one)
    angle_two = int(angle_two)
    angle_three = int(angle_three)
    print(angle_one, angle_two, angle_three)

    if angle_one > 0 and angle_two > 0 and angle_three > 0:
        if (angle_one + angle_two + angle_three) == 180:
#            print("Values correct")
            if angle_one > 0 and angle_two > 0 and angle_three > 0:
#                print("all > than 0")
                if angle_one > 90 or angle_two > 90 or angle_three > 90:
                    print("The triangle is a obtuse triangle.")
                elif angle_one == 90 or angle_two == 90 or angle_three == 90:
                    print("The triangle is a right triangle.")
                else:
                    print("The triangle is a acute triangle.")
        else:
            print("The entered values are not valid.")
    else:
        print("Angles smaller than 0 are not valid.")
else:
    print("The entered values are not valid.")
