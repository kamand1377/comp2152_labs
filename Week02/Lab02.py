import random

# Define choices array
choices = ["Rock", "Paper", "Scissors"]

# Get player input
playerChoice = input("Enter your choice (1=Rock, 2=Paper, 3=Scissors): ")
playerChoice = int(playerChoice)

# Error handling
if playerChoice < 1 or playerChoice > 3:
    print("Error: Choice must be between 1 and 3.")
else:
    # Get computer choice (random)
    computerChoice = random.randint(1, 3)

    # Array indexing (subtract 1)
    playerPick = choices[playerChoice - 1]
    computerPick = choices[computerChoice - 1]

    print("You chose:", playerPick)
    print("Computer chose:", computerPick)

    # Game logic
    if playerChoice == computerChoice:
        print("It's a tie!")
    elif playerChoice == 1 and computerChoice == 3:
        print("Rock beats Scissors - You win!")
    elif playerChoice == 2 and computerChoice == 1:
        print("Paper beats Rock - You win!")
    elif playerChoice == 3 and computerChoice == 2:
        print("Scissors beats Paper - You win!")
    else:
        print("You lose!")

    # String comparison
    if playerPick != "Rock":
        print("You didn't pick the classic Rock...")
