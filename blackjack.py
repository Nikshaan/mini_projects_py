import random

# BLACKJACK


def playgame(score1=0, score2=0):

    # considering ace as 1 only

    deck = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]

    user_card1value = random.choice(deck)
    deck.remove(user_card1value)
    user_card2value = random.choice(deck)
    deck.remove(user_card2value)
    user_cardtotal = user_card1value+user_card2value
    print("Your cards value adds upto: ", user_cardtotal)

    bot_card1value = random.choice(deck)
    deck.remove(bot_card1value)
    bot_card2value = random.choice(deck)
    deck.remove(bot_card2value)
    bot_cardtotal = bot_card1value+bot_card2value

    while True:
        choice = input("HIT or STAND: ").lower()

        if choice == "hit":
            bot_newcard = random.choice(deck)
            deck.remove(bot_newcard)
            user_newcard = random.choice(deck)
            deck.remove(user_newcard)
            bot_cardtotal += bot_newcard
            user_cardtotal += user_newcard

            print("New cards value is: ", user_cardtotal)
            if user_cardtotal > 21:
                print("BUST! You lose!")
                score2 += 1
                break
            if bot_cardtotal > 21:
                print("You Win! Computer's total exceeds 21")
                score1 += 1
                break
        elif choice == "stand":
            break
        else:
            print("Invalid choice!")
            pass
    if choice == "stand":
        if bot_cardtotal > user_cardtotal:
            print("Computer has won with", bot_cardtotal, "card value!")
            print("Your card value: ", user_cardtotal)
            score2 += 1
        elif user_cardtotal > bot_cardtotal:
            print("You have won with", user_cardtotal, "card value!")
            print("Computer's card value: ", bot_cardtotal)
            score1 += 1
        else:
            print("It's a Tie!")

    print("Your score is: ", score1)
    print("Computer's score is: ", score2)

    replay = input("Do you want to play again?(yes/no): ").lower()
    if replay == "yes":
        playgame(score1, score2)
    elif replay == "no":
        print("Your final score is: ", score1)
        print("Computer's final score is: ", score2)
        if score1 > score2:
            print("YOU WIN THE GAME!")
        elif score2 > score1:
            print("YOU LOSE THE GAME!")
        else:
            print("IT'S A TIE!")
    else:
        print("Invalid input! Exiting...")


playgame()
