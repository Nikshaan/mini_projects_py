# Hangman Game
# Total 10 guesses out of which maximum 6 can be wrong

import random


def figure(count):

    if count == 1:
        print('''
    _____________________
            |           |
            |           |
            O           |
                        |
                        |
                        |
                        |
                        |
     ___________________|
        ''')
    if count == 2:
        print('''
    _____________________
            |           |
            |           |
            O           |
            |           |
                        |
                        |
                        |
                        |
     ___________________|
        ''')
    if count == 3:
        print('''
    _____________________
            |           |
            |           |
            O           |
            |           |
           /            |
                        |
                        |
                        |
     ___________________|
        ''')
    if count == 4:
        print('''
    _____________________
            |           |
            |           |
            O           |
            |           |
           / \          |
                        |
                        |
                        |
     ___________________|
        ''')
    if count == 5:
        print('''
    _____________________
            |           |
            |           |
            O           |
            |\          |
           / \          |
                        |
                        |
                        |
     ___________________|
        ''')
    if count == 6:
        print('''
    _____________________
            |           |
            |           |
            O           |
           /|\          |
           / \          |
                        |
                        |
                        |
     ___________________|
        ''')


print(
    '''
    Welcome to Hangman!
    _____________________
            |           |
            |           |
                        |
                        |
                        |
                        |
                        |
                        |
     ___________________|
'''
)

words = ['ANT', 'BABOON', 'BADGER', 'BAT', 'BEAR', 'BEAVER', 'CAMEL', 'CAT', 'CLAM', 'COBRA', 'COUGAR', 'COYOTE', 'CROW', 'DEER', 'DOG', 'DONKEY', 'DUCK', 'EAGLE', 'FERRET', 'FOX', 'FROG', 'GOAT', 'GOOSE', 'HAWK', 'LION', 'LIZARD', 'LLAMA', 'MOLE', 'MONKEY', 'MOOSE', 'MOUSE' ,'MULE', 'NEWT', 'OTTER', 'OWL', 'PANDA', 'PARROT', 'PIGEON', 'PYTHON', 'RABBIT', 'RAM', 'RAT', 'RAVEN', 'RHINO', 'SALMON', 'SEAL', 'SHARK', 'SHEEP', 'SKUNK', 'SLOTH', 'SNAKE', 'SPIDER', 'STORK', 'SWAN', 'TIGER', 'TOAD', 'TROUT', 'TURKEY', 'TURTLE', 'WEASEL', 'WHALE', 'WOLF', 'WOMBAT', 'ZEBRA']


def playhangman(list):

    p, hm = 0, 0
    blank, wrong = [], []
    word = random.choice(list)

    for j in range(len(word)):
        blank.append('_')

    print("word is: ", "".join(blank))

    while p < 6:

        guess = input("Enter your letter: ")
        c = 0

        for i in range(len(blank)):
            if word[i] == guess.upper():
                blank[i] = guess.upper()
                c += 1

        if c == 0:
            wrong.append(guess.upper())
            p += 1
            hm += 1

        figure(hm)

        print("Your word: ", "".join(blank))

        if word == "".join(blank):
            print("You have guessed the word!")
            break

        print("Wrong guesses till now: ", wrong)


        if p == 6 or len(wrong) == 6:
            print("All guesses are Over!")
            print("The word was: ", word)
            p = 6

        print("You have ", (6 - p), " guesses left.")

    replay = input("Do you want to play again? (yes/no): ")
    if replay.lower() == 'yes':
        playhangman(words)
    else:
        print("Exiting game...")


playhangman(words)
