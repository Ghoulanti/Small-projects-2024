import random

hangman="_______\n|/     |\n|      O\n|     /|\\ \n|      /\\"
mistakes=0
guessed_letters=[]

with open("words.txt","r") as words:
    words=words.readlines()
words=[word.strip() for word in words]

word=random.choice(words)

guess=""
display=("_"*len(word))
print(" ".join(display))
x=0

while mistakes<50:
    guess=input()
    if len(guess)!=1:
        print("enter a single letter")
        continue
    else:
        if guess in guessed_letters:
            print("You already guessed this")
            continue
        else:
            if guess in word:
                x=0
                for letter in word:
                    if letter==guess:
                        display=list(display)
                        display[x]=guess
                        display= "".join(display)
                    elif letter not in guessed_letters:
                        display=list(display)
                        display[x]="_"
                        display= "".join(display)
                    x+=1
                display=display[:word.index(guess)]+guess+display[word.index(guess)+1:]
                print(" ".join(display))
                guessed_letters.append(guess)
                if "_" not in display:
                    print("You win!!!!")
                    break
                continue
            else:
                mistakes+=7
                print(hangman[0:mistakes])
                guessed_letters.append(guess)
                continue

if mistakes>49:
    print("you loose")

    print(f"the word was {word}")
