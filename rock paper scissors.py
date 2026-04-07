import random
item_list = ["rock", "paper", "scissors"]
user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
comp_choice = random.choice(item_list)
print(f"Your choice: {user_choice}")
print(f"Computer's choice: {comp_choice}")

if user_choice == comp_choice:
    print("It's a tie!")
elif (user_choice == "rock" and comp_choice == "scissors") or (user_choice == "paper" and comp_choice == "rock") or (user_choice == "scissors" and comp_choice == "paper"):
    print("You win!")
else:
    print("You lose!")