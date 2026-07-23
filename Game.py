
player1: str = input("Player 1, 'Enter  your choice ' (rock, paper, scissors): ").lower()
player2 = input("Player 2, ' Enter your choice ' (rock, paper, scissors): ").lower()

if player1 == player2:
    print("Match Tie ho gaya! Dono ne same chuna.")

elif player1 == "rock" and player2 == "scissors":
    print("player 1 Win ")
elif player1 == "scissors" and player2 == "paper":
    print("player 1 Win")
elif player1 == "paper" and player2 == "rock":
     print("player 1 Win ")
else:
    print(" Player 2  win !")