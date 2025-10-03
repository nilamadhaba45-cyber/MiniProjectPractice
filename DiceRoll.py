import random
print("\nWelCome My journey\nDice Roll Game")
user_score=0
computer_score=0
tie=0
for round in range(1,7):
    print(f"{round} Round you Attempt 5")
    user=int(input("Please enter a number 1 to 10 : "))
    computer=random.randint(1,10)
    print(f"you rolled : {user}")
    print(f"Computer rolled : {computer}")
#Win Check
    if user>computer:
        print("Congrats You win this round.")
        user_score+=1
    elif computer>user:
        print("Sorry Computer is win")
        computer_score+=1
    else:
        print("HAHA both are same so game is tie")
        tie+=1

#Final Score Check

print("\n===Final Score===")
print(f"your score is {user_score}")
print(f"computer score is {computer_score}")
print(f"Game is tie {tie} time\n")

if user_score>computer_score:
    print("Congrats you win ")
elif user_score<computer_score:
    print("You loose the game Computer win")
else:
    print("Both are win because game is tie")
