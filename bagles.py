import random
# BAGELS
print("""
    I am thinking of a 3-digit number. Try to guess what it is.
    Here are some clues:
    When I say:    That means:
    Pico         One digit is correct but in the wrong position.
    Fermi        One digit is correct and in the right position.
    Bagels       No digit is correct.
    I have thought up a number.
    You have 10 guesses to get it.
""")


def bagles(p):

    number = random.randrange(100, 1000)
    print(number)

    while True:
        guess = int(input("Enter your guess: "))
        c = 0

        if guess == number:
            print("You got it!")
            restart()
            break

        for i in range(0, 3):
            if (str(guess)[i]) == (str(number)[i]):
                print('Fermi')
                c += 1
            elif (str(number)[i]) in (str(guess)):
                print('Pico')
                c += 1

        if c == 0:
            print('Bagels')

        p += 1
        print("Number of guesses left: ", (10 - p))

        if p == 10:
            print("All guesses are over.")
            restart()


def restart():

    replay = input("Do you want to play again? (yes/no): ").lower()
    if replay == 'yes':
        bagles(p=0)
    elif replay == 'no':
        print("exiting game...")
    else:
        print("Invalid input, exiting game...")


bagles(p=0)
