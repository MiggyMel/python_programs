import random

player_wins = 0
cpu_wins = 0

print("Let's play rock, paper, or scissors!")

while player_wins < 2 and cpu_wins < 2:
    choices = ["rock", "paper" ,"scissors"]

    user_choice = input("Rock, paper, or scissors? ")
    if user_choice not in choices:
        print("Invalid option. Try rock, paper, or scissors.")
        continue
    cpu_choice = random.choice(choices)

    print(f"You chose: {user_choice}")
    print(f"The computer chose: {cpu_choice}")

    if (user_choice == "rock" and cpu_choice == "scissors") or \
    (user_choice == "paper" and cpu_choice == "rock") or \
    (user_choice == "scissors" and cpu_choice == "paper"):
        player_wins += 1
        print("You won the round")
    elif cpu_choice == user_choice:
        print("It's a tie!")
    else:
        cpu_wins += 1
        print("The computer won the round.")

    print(f"Score Player - {player_wins} | Computer - {cpu_wins}")
    
    if player_wins == 2:
        print("Congratulations! You win.")
    elif cpu_wins == 2:
        print("The computer wins.")