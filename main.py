import random


def quiz():
    correct = 0
    incorrect = 0
    num1 = 0
    while not num1 == 10:
        rannum = random.randint(1, 9)
        rannum1 = random.randint(1, 9)

        input1 = input("What is " + str(rannum1) + " times " + str(rannum) + "?: ")
        answer = str(rannum*rannum1)
        if input1 == answer:
            correct += 1
        if not input1 == answer:
            incorrect += 1
        num1 += 1
    print("You got " + str(correct) + " right and " + str(incorrect) + " wrong")


quiz()
play_again = input("Would you like to play again?: ")
if play_again == "Yes" or play_again == "yes":
    quiz()