#Now it is your turn. Write a program that expects the user to enter a sentence first and then to enter a letter. The program should output the entered sentence, removing each occurrence of the entered letter. Additionally, the output loop should be constrained to print out a maximum of 20 characters only.

#The output should look like the following (user input in bold for clarity):

#What sentence should be output? This is how it should look like
#Which letter should be removed? i
#Ths s how t should lo

#Hint: Using input(), first read in the sentence and then the letter to be removed. Create an empty string using result = "". Then iterate over the letters. If a letter is not equal to the letter to be deleted, add that letter to result (result += letter). After the for loop, output the variable result. End (break) the loop early if the length of the result string is more than 20.

letter_to_remove = input("'This is how it should look like' - choose which letter to remove from the sentence")
sentence = "This is how it should look like"
result = ""

for letter in sentence:

    if letter != letter_to_remove:
        result += letter

print(result)
