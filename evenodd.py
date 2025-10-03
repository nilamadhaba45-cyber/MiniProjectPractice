import random
print("\nWelCome to my Journey \n Even and Odd choose game")
print("Only 3 Attempt Availble\n")
computer=random.randint(1,20)
user=input("Please enter Even and Odd : ").lower()
round=0
if computer%2==0:
    com_choice="even".lower()
else:
    com_choice="odd".lower()

if com_choice==user:
    print(f"Congrats Your choice  matched with computer, Your choice {user}")        
else:
    print("Sorry You don't matched, and you losse the game")
        



