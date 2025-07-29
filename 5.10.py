"""(Find the highest score) Write a program that prompts the user to enter the number
of students and each student’s score, and displays the highest score. Assume that
the input is stored in a file named score.txt, and the program obtains the input from
the file."""
numOfStudents = eval(input("Enter the number of students:"))
highest_score = input("enter score:")


for i in range(1,numOfStudents):
    score = input("Enter score:")
    if score >= highest_score:
        highest_score = score


print("The highest score is:", score)