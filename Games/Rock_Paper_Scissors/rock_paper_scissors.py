from rich.console import *


console = Console(width=100, color_system="truecolor", emoji=True)

welcome = """WELCOME! to [i #424CDF ]@ebosetalee's[/i #424CDF]
[b #BFBF1B]Rock, Paper, Scissor Game[/b #BFBF1B]!!!"""


console.rule(welcome+ "\n\n")
console.print(""" [frame]
    Welcome to my games page!!!\n
        You are playing Rock, Paper, Scissors. 
        The mind game where we interpret numbers using our hands to mean
        Rock as 0, Paper(flat) as 5, Scissors as 2. \n
        Traditionally, the rules remain:
            - Rock beats scissors
            - Scissors beats paper
            - Paper beats rock. 

        :Sparkles:NOTE: You can type the number or the letters.:Sparkles:

        Hope you enjoy the game.... :Winking_face: [/frame]
""")

console.print(
        "\n:smiley:", "WELCOME!!!!", ":smiley:\n\n", ":Man_dancing: :Woman_dancing: " * 10,
        "\n", style="#386691 on #808080", justify="center")


player1_name  = input("Player 1, what is your first name? ")
player2_name  = input("Player 2, what is your first name? ")

player1 = input("It's Player 1's turn. Rock(0), Paper(5), Scissors(2): ")
player2 = input("Player 2. Rock(0), Paper(5), Scissors(2): ")

rock = 0
scissors = 2
paper = 5
def lowercase(strings):
    pass


while True:
    player1 = input("It's Player 1's turn. Rock(0), Paper(5), Scissors(2): ")
    player2 = input("Player 2. Rock(0), Paper(5), Scissors(2): ")
    if type(player1) == str:
        player1.lower

    if type(player2) == str:
        print("boom")
    if player1 == rock or player1 == "rock":
        if player2 == scissors:
            name = (input("Player 1 is the winner, what is your name Player 1 "))
            print("CONGRATULATIONS!!! {}".format(name))
            break
        elif player2 == paper:
            name2 = input("Player 2 is the winner, What is your name Player 2 ")
            print("CONGRATULATIONS!!! {}".format(name2))
            break
        else:
            print("Please play again rock doesn't beat rock. Thank you")
            break
    elif player1 == scissors:
        if player2 == rock:
            name3 = input("Player 2 is the winner, What is your name Player 2  ")
            print("CONGRATULATIONS!!! {}".format(name3))
            break
        elif player2 == paper:
            name4 = input("Player 1 is the winner, What is your name Player 1  ")
            print("CONGRATULATIONS!!! {}".format(name4))
            break
        else:
            print("Please play again Scissors can't beat Scissors. Thank you")
            break
    elif player1 == paper:
        if player2 == rock:
            name5 = input("Player 1 is the winner, What is your name Player 1  ")
            print("CONGRATULATIONS!!! {}".format(name5))
            break
        elif player2 == scissors:
            name6 = input("Player 2 is the winner, What is your name Player 2  ")
            print("CONGRATULATIONS!!! {}".format(name6))
            break
        else:
            print("Please play again Paper can't beat Paper. Thank you")
            break
    else:
        print("Ensure you type the correct letters or numbers. Play Again!!!")