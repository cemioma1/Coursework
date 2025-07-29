import random
import time
start_time = time.time()

correct_count= 0
total_questions = 10

for x in range (0,10):
    number1 = random.randint(1,15)
    number2 = random.randint(1,15)
    answer = eval(input(f"What is {number1} - {number2}?"))
    if answer == number1 - number2:
        print("Correct!")
        correct_count += 1
    else:
        print("Incorrect!")

print (f"You got {correct_count} out of {total_questions} Correct!")
end_time = time.time()
test_time = end_time - start_time
print(f"It took you {test_time}.2f")