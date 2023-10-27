import time
import random

def print_pause(msg_to_print):
    """
    Print a message and pause for 2 seconds.
    """
    print(msg_to_print)
    time.sleep(2)

def intro(item, option):
    """
    Display the game's introduction.
    """
    intro_message = (
        "You find yourself in a mysterious forest, with tall trees and "
        "the sound of rustling leaves all around.\n"
        "Legend has it that a hidden treasure is concealed somewhere "
        "in this forest, guarded by a fearsome creature.\n"
        "In your hand, you hold a worn-out map that marks the possible "
        "location of the treasure.\n"
        "Before you, there's a mysterious path leading deeper into the "
        "forest.\n"
        "To your right, you notice a peculiar-looking tree with an "
        "engraved symbol on its bark.\n"
        "What would you like to do?\n"
    )
    print_pause(intro_message)

def forest_path(item, option):
    """
    Explore the forest path and encounter fairies.
    """
    forest_message = (
        "You decide to follow the path into the heart of the forest.\n"
        "The further you go, the darker and more mysterious it becomes.\n"
        "Suddenly, you encounter a group of mischievous fairies who block "
        "your way.\n"
        "They demand to know why you are in their territory."
    )
    print_pause(forest_message)

    while True:
        choice2 = input("Will you (1) try to befriend the fairies or (2) stand your "
                        "ground and demand passage?\n")
        if choice2 == "1":
            befriending_message = (
                "You approach the fairies with a friendly demeanor and offer "
                "them some shiny trinkets you found earlier.\n"
                "The fairies are pleased and grant you safe passage through "
                "their forest.\n"
                "You continue on your quest, leaving the fairies behind."
            )
            print_pause(befriending_message)
            cave(item, option)
            break
        elif choice2 == "2":
            standing_ground_message = (
                "You stand your ground and insist on your right to pass.\n"
                "The fairies take offense and cast a spell on you, turning you "
                "into a toad!\n"
                "Your adventure ends here, as you can't continue as a toad."
            )
            print_pause(standing_ground_message)
            play_again()
            break
