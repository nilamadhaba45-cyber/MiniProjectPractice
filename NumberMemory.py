import random
computer=str(random.randint(100,999))
round=1
while True:
    print("\nWelCome Number Memory Game")
    user=int(input("Please enter a number : "))
    if computer==user:
        print("Are You Correct!")
        round+=1
        computer+=str(random.randint(0.9))
    else:
        print(f"Game Over! the number is {computer}")
        break
