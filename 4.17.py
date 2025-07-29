import random
user_game = eval(input("scissor (0), rock (1), paper (2):"))
computer = random.randint(0,2)

if user_game == 1 and computer == 0:
    print("The computer is scissor.You Win!")
elif user_game == 2 and computer == 1:
    print ("The computer is rock. You Win!")
elif user_game == 0 and computer == 2:
    print ("The computer is scissors. You lose!")
elif user_game == 0 and computer == 0:
    print ("The computer is scissors. You are scissors. It's a draw!")
elif user_game == 1 and computer == 1:
    print("The computer is rock. You are rock. Its a draw!")
else:
    print ("The computer is paper. You are paper. It's a draw!")