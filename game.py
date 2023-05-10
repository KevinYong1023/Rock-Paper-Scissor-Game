import random

print("-----Welcome to the game------")
choices = ('Rock', 'Paper', 'Scissor')


def userInfo():
    username = input("What is your name?: ")
    return username


name = userInfo()


def gameStarts():
    cpuChoice = random.choice(choices)
    while True:
        userChoice = input("Insert one: ")
        if userChoice in choices:
            checkResult(userChoice, cpuChoice)
            break
        else:
            print("You got a wrong one")


def checkResult(user, cpu):
    print("CPU choices", cpu)
    if (user == "Rock" and cpu == 'Scissor') or (user == "Scissor" and cpu == 'Paper') or (
            user == 'Paper' and cpu == 'Rock'):
        print("YOU WIN !!!")
    elif (cpu == "Rock" and user == 'Scissor') or (cpu == "Scissor" and user == 'Paper') or (
            cpu == 'Paper' and user == 'Rock'):
        print("YOU LOSE !!!")
    else:
        restartGame()


def restartGame():
    while True:
        restart = input("TIE !!!, Let's try again (Y/N)?:").upper()
        if restart == 'Y':
            gameStarts()
            break
        elif restart == 'N':
            print("Thanks for playing !")
            break
        else:
            print("Please enter a valid answer")
            break


def userDecision():
    print("Hello", name)
    while True:
        decision = input("Do you want to play?(Y/N): ").upper()
        if decision == 'Y':
            gameStarts()
            break
        elif decision == 'N':
            print("Thanks for playing")
            break
        else:
            print("Please insert the correct option.")


userDecision()
