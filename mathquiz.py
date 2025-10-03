import random
print("\nWelCome to My Journey\nMathQuiz Game")
print("---WelCome to MarhQuiz Game---")
score=0
for round in range(1,6):
    #Random Numbers
    num1=random.randint(1,50)
    num2=random.randint(1,50)
    #random operator
    operator=random.choice(["+","-","*"])
    #Answer calculate
    if operator=="+":
        correct_answer=num1+num2
    elif operator=="-":
        correct_answer=num1-num2
    else:
        correct_answer=num1*num2
    
    #Show Question
    print(f"Q{round}: What is {num1} {operator} {num2} ?")
    user_answer=int(input("Please Give me answer : "))

    #check answer
    if correct_answer==user_answer:
        print("Correct!")
        score+=1
    else:
        print(f"Wrong Answer !,correct answer was {correct_answer}")
    
#final score
print("===Final Score===")
print(f"Your total score is {score}/5={score/5}%")
if score==5:
    print("Excellent")
elif score>=3:
    print("Good")
else:
    print("Need practice")

        