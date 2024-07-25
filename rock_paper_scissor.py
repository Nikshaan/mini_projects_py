# rock-paper-scissor game

import random


def playgame(p=0, c=0):

    list = ['rock', 'paper', 'scissor']

    while True:
        computer = random.choice(list)
        player = input("Enter your choice (rock/ paper/ scissor): ")

        if player.lower() == computer:
            print("It is a Tie!, Computer played: ", computer)

        elif player.lower() == 'rock':
            if computer == 'scissor':
                print("You Win, computer played: ", computer)
                p += 1
            elif computer == 'paper':
                print("You Lose, computer played: ", computer)
                c += 1

        elif player.lower() == 'scissor':
            if computer == 'paper':
                print("You Win, computer played: ", computer)
                p += 1
            elif computer == 'rock':
                print("You Lose, computer played: ", computer)
                c += 1

        elif player.lower() == 'paper':
            if computer == 'rock':
                print("You Win, computer played: ", computer)
                p += 1
            elif computer == 'scissor':
                print("You Lose, computer played: ", computer)
                c += 1

        else:
            print("Invalid input!")

        print("Your wins: ", p)
        print("Computer's wins: ", c)

        replay = input("Do you want to play again? (yes/no): ")

        if replay.lower() == 'yes':
            playgame(p, c)

        else:
            if p == c:
                print("Game ends in a Tie!")
            elif p > c:
                print("You have Won the Game!")
            else:
                print("Computer wins the Game!")

        break


playgame()
