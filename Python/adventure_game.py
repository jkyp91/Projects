import random
import time
import sys

locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

exits = [{"Q": 0},
         {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         {"N": 5, "Q": 0},
         {"W": 1, "Q": 0},
         {"N": 1, "W": 2, "Q": 0},
         {"W": 1, "S": 1, "Q": 0}]


def delay_print(phrase):
    for letter in phrase:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)


loc = 1
while True:
    # availableExits = ""
    # for direction in exits[loc].keys():
    #     availableExits += direction + ", "
    availableExits = ", ".join(exits[loc].keys())

    print(locations[loc])

    if loc == 0:
        break

    if loc == 3:
        delay_print("A wild rat approaches"
                    ". The rat has 100 hp, hit it with your sword[S] or run away[R]: ")
        action = input("").upper()
        rat_hp = 100
        sword_hit = random.randrange(40, 60)
        if action == "S":
            while rat_hp > 0:
                rat_hp -= sword_hit
                print("You hit the rat for {}".format(sword_hit))
                print("The rat has {} health".format(rat_hp))
                if rat_hp > 0:
                    input("Hit it again [s]" + "\n")
                if rat_hp - sword_hit <= 0:
                    sword_hit = rat_hp
            else:
                print("Good Job! the rat is dead")
        elif action == "R":
            print("You got away safely... pussy.")
            direction = input("Available exits are " + availableExits.upper())
            print()
        else:
            input("Do something: ")

    if loc == 5:
        delay_print("You are confronted by Bigfoot"
                    ". \"In order to proceed, Please guess my favourite body part\" he says, you have"
                    " 3 guesses: " + "\n")
        answer = "foot"
        guess = input("")
        count_guesses = 1
        guess_limit = 3
        while guess != answer and guess_limit > count_guesses:
            print("{} more guesses until I eat your {}".format(guess_limit - count_guesses, guess))
            count_guesses += 1
            guess = input("Try again" + "\n")
            if guess == answer:
                print("That sucks, you got it")
            else:
                print("I'm going to enjoy eating your.... Hey, get back here!")
                print("You got away safely")


    direction = input("Available exits are " + availableExits.upper() + '\n').upper()
    print()
    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("You cannot go in that direction")
