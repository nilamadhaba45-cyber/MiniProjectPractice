'''Guess the Word (Mini Hangman)
Computer ek word select karega (jaise "apple")
User ek-ek letter guess kare
Agar letter hai to show karo, warna chances kam ho jaayenge
User ke paas 6 lives'''

import random
#Words listed fit computer
words=["apple","grape","orange","mango","banana"]
word=random.choice(words)

lives=6
guess_letter=[]                   #Stored guessing correct letter
display = ["_"] * len(word)       #Word ki jagha "_" use kiya display hone ke liye

print("\nWelcome to Guess the Word (Mini Hangman)")
print("You have 6 lives. Try to guess the word!")
print("Word:"," ".join(display))     #Starting mein blank dikhega

#Game loop start
while lives>0 and "_" in display:
    guess=input("\nEnter a letter : ").lower()
    if guess in guess_letter:
        print("You already guessed that letter. Try another")
        continue
    guess_letter.append(guess)

    if guess in word:
        print("You guessed correct word !")
        for  i in range(len(word)):       #correct letter check in word
            if word[i]==guess:
                display[i] = guess
    else:
        lives-=1
        print(f"You guess wrong your lives in {lives}")
    print("word:"," ".join(display))

#Result Check
if "_" not in display:
    print("\nCongratulation you guessed the word !")
else:
    print(f"\nGame Over, the word was : {word}")

    

