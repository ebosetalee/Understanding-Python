from rich.console import *


console = Console(width=100, color_system="truecolor", emoji=True)

welcome = """\nWELCOME! to [i #424CDF ]@ebosetalee's[/i #424CDF]
[b #BFBF1B]Rock, Paper, Scissor Game !!![/b #BFBF1B]"""


console.rule(welcome + "\n\n")
console.print(""" [frame #FFE5B4]
        Welcome to my games page!!!\n
            You are playing Rock, Paper, Scissors. 
            The mind game where we interpret numbers using our hands to mean
            Rock as 0, Paper(flat) as 5, Scissors as 2. \n
            Traditionally, the rules remain:
                - Rock beats scissors
                - Scissors beats paper
                - Paper beats rock. 

         :Sparkles: NOTE: You can type the number or the letters. :Sparkles:

            Don't forget Y or N!

        Hope you enjoy the game.... :Winking_face: [/frame #FFE5B4]
""")

console.print(
    "\n:smiley:", "WELCOME!!!!", ":smiley:\n\n", ":Man_dancing: :Woman_dancing: " * 10,
    "\n", style="#386691 on #808080", justify="center")


player1_name = input(
    "\nHii.. Player 1, what is your first name? ").capitalize()
player2_name = input(
    "\nHello.. Player 2, what is your first name? ").capitalize()

rock = 0
scissors = 2
paper = 5


def lowercase(player):
    play = console.input(
        "\n[blue]It's {}'s turn[/blue]. Rock(0), Paper(5), Scissors(2): ".format(player))
    try:
        play = int(play)
    except ValueError:
        return play.lower()
    finally:
        return play


def replay(answer):
    if answer.lower() == "y":
        return main_game()
    console.rule("Thank you for playing!! BYE.....")


def main_game():
    player1 = lowercase(player1_name)
    player2 = lowercase(player2_name)

    if player1 == rock or player1 == "rock":
        if player2 == scissors or player2 == "scissors":
            console.print(
                "\n[b green]CONGRATULATIONS!!! {} won![/b green]\n".format(player1_name))
            replay(console.input(
                "[b yellow]Do you wanna play again?(Y/N)[/b yellow] "))
        elif player2 == paper or player2 == "paper":
            console.print(
                "\n[b green]CONGRATULATIONS!!! {} won![/b green]\n".format(player2_name))
            replay(console.input(
                "[b yellow]Do you wanna play again?(Y/N)[/b yellow] "))
        else:
            console.print(
                "\n[b red]Please play again rock doesn't beat rock. Thank you[/b red]\n")
            replay(console.input(
                "[b yellow]Do you wanna play again?(Y/N)[/b yellow] "))

    elif player1 == scissors or player1 == "scissors":
        if player2 == rock or player2 == "rock":
            console.print(
                "\n[b green]CONGRATULATIONS!!! {} won![/b green]\n".format(player2_name))
            replay(console.input(
                "[b yellow]Do you wanna play again?(Y/N)[/b yellow] "))
        elif player2 == paper or player2 == "paper":
            console.print(
                "\n[b green]CONGRATULATIONS!!! {} won![/b green]\n".format(player1_name))
            replay(console.input(
                "[b yellow]Do you wanna play again?(Y/N)[/b yellow] "))
        else:
            console.print(
                "\n[b red]Please play again Scissors can't beat Scissors. Thank you\n")
            replay(console.input(
                "[b yellow]Do you wanna play again?(Y/N)[/b yellow] "))

    elif player1 == paper or player1 == "paper":
        if player2 == rock or player2 == "rock":
            console.print(
                "\n[b green]CONGRATULATIONS!!! {} won![/b green]\n".format(player1_name))
            replay(console.input(
                "[b yellow]Do you wanna play again?(Y/N)[/b yellow] "))
        elif player2 == scissors or player2 == "scissors":
            console.print(
                "\n[b green]CONGRATULATIONS!!! {} won![/b green]\n".format(player2_name))
            replay(console.input(
                "[b yellow]Do you wanna play again?(Y/N)[/b yellow] "))
        else:
            console.print(
                "\n[b red]Please play again Paper can't beat Paper. Thank you[/b red]\n")
            replay(console.input(
                "[b yellow]Do you wanna play again?(Y/N)[/b yellow] "))

    else:
        print("\nEnsure you type the correct letters or numbers. Play Again!!!")


main_game()
