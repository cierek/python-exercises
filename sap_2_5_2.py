#Write a program that lets the user input a two-dimensional matrix (Hint: you could use a list of lists to store the matrix). The program should first ask the user how many rows and columns the matrix should contain. Next, the program should ask the user for the elements of the matrix. Your program should read the values from the user row by row. If, for example, the matrix has the dimension 2 by 3, the values should be read as follows:

#First row, first value
#First row, second value
#First row, third value
#Second row, first value
#Second row, second value
#Second row, third value
#Finally, the program should calculate and print the sums of the values in each row.

#Below is an example execution of the program:

#Please enter the number of rows in the matrix: 2
#Please enter the number of columns in the matrix: 3
#Enter the matrix values:
#Value: 1
#Value: 2
#Value: 3
#Value: 4
#Value: 5
#Value: 6
#Sum of row: 6
#Sum of row: 15

number_of_rows = int(input("Please enter the number of rows in the matrix:"))
number_of_columns = int(input("Please enter the number of columns in the matrix:"))
print("Enter the matrix values:")

list_matrix = []

for i in range(number_of_rows):
    list_matrix.append([])
    for j in range(number_of_columns):
        user_input = int(input("Value:"))
        list_matrix[i].append(user_input)


for i in list_matrix:
    print("Sum of row:", sum(i))
