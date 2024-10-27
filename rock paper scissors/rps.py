import random

han = {
    "paper": "scissors",
    "rock": "paper",
    "scissors": "rock"
}

try:
    with open("record.txt", "r") as record_file:
        record = int(record_file.read().strip())
except (FileNotFoundError, ValueError):
    record = 0

print(f"Hello and Welcome to rock paper scissors. You have a high score of {record}")
score = 0
hands = ["rock", "paper", "scissors"]

while True:
    play = input("Do you want to play? (yes/no) ").strip().lower()
    if play in ["no", "n"]:
        print("Goodbye!")
        break
    elif play not in ["yes", "y"]:
        print("Invalid input. Please type 'yes' or 'no'.")
        continue

    while True:
        hand = input("rock, paper, or scissors? ").strip().lower()
        if hand not in hands:
            print("Invalid input, please choose 'rock', 'paper', or 'scissors'.")
            continue

        computer = random.choice(hands)
        print(f"Computer chose: {computer}")


        if hand == computer:
            print(f"Draw :|\nScore={score}")
        elif han[hand] == computer:
            print("You lose :(\nYour score went back to 0")
            score = 0
        else:
            score += 1
            if score > record:
                record = score
                with open("record.txt", "w") as record_file:
                    record_file.write(str(score))
            print(f"You win :D\nYour score is {score} and your record is {record}")

        play_again = input("Do you want to play again? (yes/no) ").strip().lower()
        if play_again in ["no", "n"]:
            print("Goodbye!")
            break

