from rich.console import *
import getpass

console = Console(width=100, color_system="truecolor", emoji=True)

welcome = """\nWELCOME! to [i #424CDF ]@ebosetalee's[/i #424CDF]
[b #BFBF1B]Rock, Paper, Scissor Game !!![/b #BFBF1B]"""


console.rule(welcome + "\n\n")
console.print(""" [frame #FFE5B4]
        Welcome to my games page!!!\n
            You are playing Rock, Paper, Scissor. 
            The mind game where we interpret numbers using our hands to mean
            Rock as 0, Paper(flat) as 5, Scissor as 2. \n
            Traditionally, the rules remain:
                - Rock beats scissor
                - Scissor beats paper
                - Paper beats rock. 

         :Sparkles: NOTE: You can type the number or the letters. :Sparkles:

            Don't forget Y or N!

        Hope you enjoy the game.... :Winking_face: [/frame #FFE5B4]
""")

console.print(
    "\n:smiley:", "WELCOME!!!!", ":smiley:\n\n", ":Man_dancing: :Woman_dancing: " * 10,
    "\n", style="#386691 on #808080", justify="center")

rock = 0
scissor = 2
paper = 5


class RPSGame:
    def __init__(self):
        self.player1_name = input(
            "\nHii.. Player 1, what is your first name? ").capitalize()
        self.player2_name = input(
            "\nHello.. Player 2, what is your first name? ").capitalize()

    def lowercase(self, player):
        play = getpass.getpass(
            prompt="\nIt's {}'s turn. Rock(0), Paper(5), Scissor(2): ".format(player))
        try:
            play = int(play)
        except ValueError:
            return play.lower()
        finally:
            return play

    def replay(self, answer):
        if answer.lower() == "y":
            return self.main_game()
        console.rule("Thank you for playing!! BYE.....")

    def main_game(self):
        player1 = self.lowercase(self.player1_name)
        player2 = self.lowercase(self.player2_name)

        if player1 == rock or player1 == "rock":
            if player2 == scissor or player2 == "scissor":
                console.print(
                    "\n[b green]CONGRATULATIONS!!! {0} won![/b green]... [#B78628]{1} beats {2}[/#B78628]\n".format(
                        self.player1_name, player1, player2))
                self.replay(console.input(
                    "[b yellow]Do you wanna play again?(Y/N)[/b yellow] "))
            elif player2 == paper or player2 == "paper":
                console.print(
                    "\n[b green]CONGRATULATIONS!!! {0} won![/b green]... [#B78628]{1} beats {2}[/#B78628]\n".format(
                        self.player2_name, player2, player1))
                self.replay(console.input(
                    "[b yellow]Do you wanna play again?(Y/N)[/b yellow] "))
            elif player2 == rock or player2 == "rock":
                console.print(
                    "\n[b red]Please play again Scissor can't beat Scissor. Thank you\n")
                self.replay(console.input(
                    "[b yellow]Do you wanna play again?(Y/N)[/b yellow] "))
            else:
                print("\nEnsure you type the correct letters or numbers, {0} played {1} and {2} played {3}. Play Again!!!".format(
                    self.player1_name, player1, self.player2_name, player2))

        elif player1 == scissor or player1 == "scissor":
            if player2 == rock or player2 == "rock":
                console.print(
                    "\n[b green]CONGRATULATIONS!!! {0} won![/b green]... [#B78628]{1} beats {2}[/#B78628]\n".format(
                        self.player2_name, player2, player1))
                self.replay(console.input(
                    "[b yellow]Do you wanna play again?(Y/N)[/b yellow] "))
            elif player2 == paper or player2 == "paper":
                console.print(
                    "\n[b green]CONGRATULATIONS!!! {0} won![/b green]... [#B78628]{1} beats {2}[/#B78628]\n".format(
                        self.player1_name, player1, player2))
                self.replay(console.input(
                    "[b yellow]Do you wanna play again?(Y/N)[/b yellow] "))
            elif player2 == scissor or player2 == "scissor":
                console.print(
                    "\n[b red]Please play again Scissor can't beat Scissor. Thank you\n")
                self.replay(console.input(
                    "[b yellow]Do you wanna play again?(Y/N)[/b yellow] "))
            else:
                print("\nEnsure you type the correct letters or numbers, {0} played {1} and {2} played {3}. Play Again!!!".format(
                    self.player1_name, player1, self.player2_name, player2))

        elif player1 == paper or player1 == "paper":
            if player2 == rock or player2 == "rock":
                console.print(
                    "\n[b green]CONGRATULATIONS!!! {0} won![/b green]... [#B78628]{1} beats {2}[/#B78628]\n".format(
                        self.player1_name, player1, player2))
                self.replay(console.input(
                    "[b yellow]Do you wanna play again?(Y/N)[/b yellow] "))
            elif player2 == scissor or player2 == "scissor":
                console.print(
                    "\n[b green]CONGRATULATIONS!!! {0} won![/b green]... [#B78628]{1} beats {2}[/#B78628]\n".format(
                        self.player2_name, player2, player1))
                self.replay(console.input(
                    "[b yellow]Do you wanna play again?(Y/N)[/b yellow] "))
            elif player2 == paper or player2 == "paper":
                console.print(
                    "\n[b red]Please play again Paper can't beat Paper. Thank you[/b red]\n")
                self.replay(console.input(
                    "[b yellow]Do you wanna play again?(Y/N)[/b yellow] "))
            else:
                print("\nEnsure you type the correct letters or numbers, {0} played {1} and {2} played {3}. Play Again!!!".format(
                    self.player1_name, player1, self.player2_name, player2))

        else:
            print("\nEnsure you type the correct letters or numbers, {0} played {1} and {2} played {3}. Play Again!!!".format(
                self.player1_name, player1, self.player2_name, player2))


rpsgame = RPSGame()
rpsgame.main_game()
