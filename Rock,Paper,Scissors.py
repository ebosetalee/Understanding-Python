# Make a two player Rock- Paper - Scissors game.(Hint: Ask for player plays
# (using input), compare them, print out a message of congratulations to the winner,
# and ask if the players want to start a new game.)
# Remember the rules:
# Rock beats scissors
# Scissors beats paper
# Paper beats rock. 
player1 = int(input("Please type the equivalent number "))
player2 = int(input("Please type the equivalent number "))

rock = 0
scissors = 2
paper = 5

while True:
    if player1 == rock:
        if player2 == scissors:
            name = (input("Player 1 is the winner, what is your name Player 1 "))
            print("CONGRATUATIONS!!! {}".format(name))
            break
        elif player2 == paper:
            name2 = input("Player 2 is the winner, What is your name Player 2 ")
            print("CONGRATUATIONS!!! {}".format(name2))   
            break
        else:
            print("Please play again rock doesn't beat rock. Thank you")  
            break
    elif player1 == scissors:
        if player2 == rock:
            name3 = input("Player 2 is the winner, What is your name Player 2  ")
            print("CONGRATUATIONS!!! {}".format(name3))   
            break
        elif player2 == paper:
            name4 = input("Player 1 is the winner, What is your name Player 1  ")
            print("CONGRATUATIONS!!! {}".format(name4))
            break
        else:
            print("Please play again Scissors can't beat Scissors. Thank you")
            break
    else:
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