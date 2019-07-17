import time
import random
import sys


#this is where I put global functions
items = []


def pirate_game():
    pirate_field()


def troll_game():
    troll_field()


def pause():
    time.sleep(2)


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


def intro():
    print_pause("You find yourself standing in an open field, filled with "
                "grass and yellow wildflowers.\n")


def pirate_field():
    print_pause("Rumor has it that a pirate is somewhere around here, and has "
                "been terrifying the nearby village.\n")
    pirate_cave_house_choice()


def troll_field():
    print_pause("Rumor has it that a troll is somewhere around here, and has "
                "been terrifying the nearby village.\n")
    troll_cave_house_choice()


def pirate_cave_house_choice():
    print_pause("In front of you is a house.\n")
    print_pause("To your right is a dark cave.\n")
    if "sword" not in items:
        print_pause("In your hand you hold your trusty (but not very "
                    "effective) dagger.\n")
    else:
        print_pause("What would you like to do?\n")
    pause()
    pirate_field_choice()


def troll_cave_house_choice():
    print_pause("In front of you is a house.\n")
    print_pause("To your right is a dark cave.\n")
    if "sword" not in items:
        print_pause("In your hand you hold your trusty (but not very "
                    "effective) dagger.\n")
    else:
        print_pause("What would you like to do?\n")
    pause()
    troll_field_choice()


def pirate_cave():
    print_pause("You peer cautiously into the cave.\n")
    print_pause("It turns out to be only a very small cave.\n")
    if "sword" not in items:
        print_pause("Your eye catches a glint of metal behind a rock.\n")
        print_pause("You have found the magical Sword of Ogoroth!\n")
        print_pause("You discard your silly old dagger and take the sword with"
                    " you.\n")
        print_pause("You walk back out to the field.\n")
        items.append("sword")
        pirate_cave_house_choice()
    else:
        print_pause("There is only a tiny, tiny dagger, so small only a baby "
                    "should wield, you go back to the field")
        pirate_cave_house_choice()


def troll_cave():
    print_pause("You peer cautiously into the cave.\n")
    print_pause("It turns out to be only a very small cave.\n")
    if "sword" not in items:
        print_pause("Your eye catches a glint of metal behind a rock.\n")
        print_pause("You have found the magical Sword of Ogoroth!\n")
        print_pause("You discard your silly old dagger and take the sword with"
                    " you.\n")
        print_pause("You walk back out to the field.\n")
        items.append("sword")
        troll_cave_house_choice()
    else:
        print_pause("There is only a tiny, tiny dagger, so small only a baby "
                    "should wield, you go back to the field")
        troll_cave_house_choice()


def pirate_field_choice():
    choice = input("Enter 1 to knock on the door of the house.\n"
                   "Enter 2 to peer into the cave.\n\n"
                   "What would you like to do?\n\n"
                   "(Please enter 1 or 2.)\n").lower()
    if choice == '1':
        pirate_house()
    elif choice == '2':
        pirate_cave()
    else:
        print_pause("That'\s not an option you scaredy cat!!\n")
        pirate_field_choice()


def troll_field_choice():
    choice = input("Enter 1 to knock on the door of the house.\n"
                   "Enter 2 to peer into the cave.\n\n"
                   "What would you like to do?\n\n"
                   "(Please enter 1 or 2.)\n").lower()
    if choice == '1':
        troll_house()
    elif choice == '2':
        troll_cave()
    else:
        print_pause("That'\s not an option you scaredy cat!!\n")
        troll_field_choice()


def pirate_house():
    print_pause("You approach the door of the house.\n")
    print_pause("You are about to knock when the door opens and out steps a "
                "pirate.\n")
    print_pause("Eep! This is the pirate's house!\n")
    print_pause("The pirate attacks you!\n")
    if "sword" in items:
        choice = input("Would you like to (1) fight or (2) run "
                       "away?\n").lower()
        if choice == '1':
            print_pause("As the pirate moves to attack, you unsheath your new "
                        "sword.\n")
            print_pause("The Sword of Ogoroth shines brightly in your hand as "
                        "you brace yourself for the attack.\n")
            print_pause("But the pirate takes one look at your shiny new toy "
                        "and runs away!\n")
            print_pause("You have rid the town of the pirate. You are "
                        "victorious!\n")
            again = input("Would you like to play again? (y/n)\n").lower()
            if "y" in again:
                start()
            else:
                print("laters..................\n")
                sys.exit()
        elif choice == '2':
            print_pause("You run back into the field. Luckily, you don't seem "
                        "to have been followed.\n")
        else:
            print_pause("cmon scaredy cat, you need to make a real decision\n")
            pirate_fight_choice()
    else:
        print_pause("You feel a bit under-prepared for this, what with only "
                    "having a tiny dagger.\n")
        choice = input("Would you like to (1) fight or (2) run "
                       "away?\n").lower()
        if choice == '1':
            print_pause("You do your best...\n")
            print_pause("but your dagger is no match for the pirate.\n")
            print_pause("You have been defeated!\n")
            again = input("Would you like to play again? (y/n)").lower()
            if "y" in again:
                start()
            else:
                print("laters..................")
                sys.exit()
        elif choice == '2':
            pirate_run_away()
        else:
            print_pause("cmon scaredy cat, you need to make a real decision\n")
            pirate_fight_choice()


def troll_house():
    print_pause("You approach the door of the house.\n")
    print_pause("You are about to knock when the door opens and out steps a "
                "troll.\n")
    print_pause("Eep! This is the troll's house!\n")
    print_pause("The troll attacks you!\n")
    if "sword" in items:
        choice = input("Would you like to (1) fight or (2) run "
                       "away?\n").lower()
        if choice == '1':
            print_pause("As the troll moves to attack, you unsheath your new "
                        "sword.\n")
            print_pause("The Sword of Ogoroth shines brightly in your hand as "
                        "you brace yourself for the attack.\n")
            print_pause("But the troll takes one look at your shiny new toy "
                        "and runs away!\n")
            print_pause("You have rid the town of the troll. You are "
                        "victorious!\n")
            again = input("Would you like to play again? (y/n)\n").lower()
            if "y" in again:
                start()
            else:
                print("laters..................\n")
                sys.exit()
        elif choice == '2':
            print_pause("You run back into the field. Luckily, you don't seem "
                        "to have been followed.\n")
        else:
            print_pause("cmon scaredy cat, you need to make a real decision\n")
            troll_fight_choice()
    else:
        print_pause("You feel a bit under-prepared for this, what with only "
                    "having a tiny dagger.\n")
        choice = input("Would you like to (1) fight or (2) run "
                       "away?\n").lower()
        if choice == '1':
            print_pause("You do your best...\n")
            print_pause("but your dagger is no match for the troll.\n")
            print_pause("You have been defeated!\n")
            again = input("Would you like to play again? (y/n)").lower()
            if "y" in again:
                start()
            else:
                print("laters..................")
                sys.exit()
        elif choice == '2':
            troll_run_away()
        else:
            print_pause("cmon scaredy cat, you need to make a real decision\n")
            troll_fight_choice()


def pirate_run_away():
    print_pause("You run back into the field. Luckily, the pirate hasn't "
                "chased after you!!")
    pirate_cave_house_choice()


def troll_run_away():
    print_pause("You run back into the field. Luckily, the troll hasn't "
                "followed you!!")
    troll_cave_house_choice()


def start():
    game_choice = [pirate_game(), troll_game()]
    intro()
    random.choice(game_choice)


start()
