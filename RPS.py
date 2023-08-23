import random

def rock_paper_scissors():
    usrInput = input("Pick rock, paper, or scissors: ")
    rps = ['rock','paper','scissors']
    computerPick = random.choice(rps)
    
    if usrInput == computerPick:
        print("you picked "+usrInput+"!")
        print("the computer also picked "+computerPick+"!")
        print("it was a tie!")
    elif usrInput == "rock" and computerPick == "scissors" or usrInput == "paper" and computerPick == "rock" or usrInput == "scissors" and computerPick == "paper":
        print("You picked "+usrInput+"!")
        print("The computer picked "+computerPick+"!")
        print("YOU WIN!")
    else:
        print("You picked "+usrInput+"!")
        print("The computer picked "+computerPick+"!")
        print("YOU loose!")
        
while True:
    rock_paper_scissors()
    if input("would you like to play again (y/n):") == "n":
        break