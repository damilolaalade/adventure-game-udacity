import random
import time

# 2sec delay on messages to be printed on screen


def print_msg(msg_to_print):
    print(msg_to_print)
    time.sleep(1)
# introduction and description of the start point of game to player


def intro(items, options):
    print_msg("You find yourself standing in an open field, filled with grass"
              " and yellow wildflowers.\n")
    print_msg("Rumor has it that a " + options + " is somewhere around here,"
              "and has been terrifying the nearby village.\n")
    print_msg("In front of you is a house.\n")
    print_msg("To your right is a dark cave.\n")
    print_msg("In your hand you hold your trusty (but not very effective)"
              " dagger.\n")

# what happens when player chooses to fight


def fight(items, options):
    if "sword" in items:
        print_msg("\nAS the " + options + " moves to attack")
        print_msg("\nThe Sword of Ogoroth shines brightly in "
                  "your hand as you brace yourself for the "
                  "attack.")
        print_msg("\nBut the " + options + "takes one look at "
                  "your shiny new toy and runs away!")
        print_msg("\nYou have rid the town of the " + options +
                  ". You are victorious!\n")
    else:
        print_msg("\nYou do your best...")
        print_msg("but your dagger is no match for the"
                  + options + ".")
        print_msg("\nYou have been defeated!\n")
        repeat_game()

# what happens when player chooses to run away


def field(items, options):
    print_msg("\nYou run back into the field. "
              "\nLuckily, you don't seem to have been "
              "followed.\n")

# what happens when player chooses to go into the house


def house(items, options):
    print_msg("\nYou approach the door of the house")
    print_msg("\nYou are about to knock when the door"
              "opens and steps out a " + options + ". ")
    print_msg("\nEep! This is the " + options + " house.")
    print_msg("\nThe " + options + " attacks you!\n")
    if "sword" not in items:
        print_msg("You are underprepared for this"
                  " what with only having a tiny dagger\n")
    while True:
        try:
            entry_choice = int(input("Would you like to (1) fight or (2)"
                                     " run away?"))
        except ValueError:
            print_msg("That's not an option\n")
            continue
        if entry_choice == 1:
            fight(items, options)
        elif entry_choice == 2:
            field(items, options)
        else:
            print_msg("That's not an option")
            entry(items, options)

# what happens when player chooses to go into the cave


def cave(items, options):
    if "sword" in items:
        print_msg("\nYou peer cautiously into the cave.")
        print_msg("\nYou've been here before, and gotten all"
                  " the good stuff. It's just an empty cave"
                  " now.")
        print_msg("\nYou walk back to the field.\n")
    else:
        print_msg("\nYou peer cautiously into the cave.")
        print_msg("\nIt turns out to be only a very small cave.")
        print_msg("\nYour eye catches a glint of metal behind a "
                  "rock.")
        print_msg("\nYou have found the magical Sword of Ogoroth!")
        print_msg("\nYou discard your silly old dagger and take "
                  "the sword with you.")
        print_msg("\nYou walk back out to the field.\n")
        items.append("sword")
    entry(items, options)

# validation of player's input


def entry(items, options):
    print_msg("Enter 1 to knock on the door of the house\n")
    print_msg("Enter 2 to peer into the cave\n")
    print_msg("What would you like to do?")
    while True:
        try:
            entry_points = int(input("(Please enter 1 or 2.)"))
        except ValueError:
            print_msg("That's not an option\n")
            continue
        if entry_points == 1:
            house(items, options)
        elif entry_points == 2:
            cave(items, options)
        else:
            print_msg("That's not an option")
            entry(items, options)


def repeat_game():
    while True:
        try:
            repeat = input("Would you like to play again? (y/n)").lower()
        except ValueError:
            print_msg("That's not an option\n")
            continue
        if repeat == "y":
            print_msg("\n\n\nExcellent! Restarting the game ...\n\n\n")
            play_game()
        elif repeat == "n":
            print_msg("\n\n\nThanks for playing! See you next time.\n\n\n")
            exit(0)
        else:
            print_msg("That's not an option")
            repeat_game()


def play_game():
    items = []
    options = random.choice(["wicked fairy", "pirate", "dragon", "troll",
                            "gorgon"])
    intro(items, options)
    entry(items, options)


play_game()
