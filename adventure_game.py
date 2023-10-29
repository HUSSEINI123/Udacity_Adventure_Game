import time
import random

def print_pause(msg_to_print):
    """
    Print a message and pause for 2 seconds.
    """
    print(msg_to_print)
    time.sleep(2)import time
import random

def print_pause(msg_to_print):
    """
    Print a message and pause for 2 seconds.
    """
    print(msg_to_print)
    time.sleep(2)

def valid_input(prompt, options):
    """
    Get and validate user input from a list of options.
    """
    while True:
        response = input(prompt).lower()
        if response in options:
            return response
        print("Invalid input!")

def intro():
    """
    Display the game's introduction.
    """
    print_pause("You find yourself in a mysterious forest, with tall trees and "
                "the sound of rustling leaves all around.")
    print_pause("Legend has it that a hidden treasure is concealed somewhere "
                "in this forest, guarded by a fearsome creature.")
    print_pause("In your hand, you hold a worn-out map that marks the possible "
                "location of the treasure.")
    print_pause("Before you, there's a mysterious path leading deeper into the "
                "forest.")
    print_pause("To your right, you notice a peculiar-looking tree with an "
                "engraved symbol on its bark.")
    print_pause("What would you like to do?")

def forest_path(item, option):
    """
    Explore the forest path and encounter fairies.
    """
    print_pause("You decide to follow the path into the heart of the forest.")
    print_pause("The further you go, the darker and more mysterious it becomes.")
    print_pause("Suddenly, you encounter a group of mischievous fairies who block "
                "your way.")
    print_pause("They demand to know why you are in their territory.")

    choice2 = valid_input("Will you (1) try to befriend the fairies or (2) stand your "
                        "ground and demand passage?", ['1', '2'])
    if choice2 == "1":
        print_pause("You approach the fairies with a friendly demeanor and offer "
                    "them some shiny trinkets you found earlier.")
        print_pause("The fairies are pleased and grant you safe passage through "
                    "their forest.")
        print_pause("You continue on your quest, leaving the fairies behind.")
        cave(item, option)  # Pass the required arguments.
    elif choice2 == "2":
        print_pause("You stand your ground and insist on your right to pass.")
        print_pause("The fairies take offense and cast a spell on you, turning you "
                    "into a toad!")
        print_pause("Your adventure ends here, as you can't continue as a toad.")
        play_again()

# Create similar functions for enchanted_tree(), cave(), and treasure().

def play_again():
    """
    Restart or quit the game.
    """
    again = valid_input("Would you like to embark on another adventure? (y/n)", ['y', 'n'])
    if again == "y":
        print_pause("\n\n\nExcellent! Starting a new adventure...\n\n\n")
        play_game()
    elif again == "n":
        print_pause("\n\n\nThank you for playing! See you next time.\n\n\n")

def play_game():
    item = []
    option = random.choice(["ancient guardian", "enigmatic spirit", "mystical "
                        "beast", "shadowy figure", "guardian of secrets"])
    intro()
    forest_path(item, option)  # Pass the required arguments.

if __name__ == "__main__":
    play_game()

def valid_input(prompt, options):
    """
    Get and validate user input from a list of options.
    """
    while True:
        response = input(prompt).lower()
        if response in options:
            return response
        print("Invalid input!")

def intro():
    """
    Display the game's introduction.
    """
    print_pause("You find yourself in a mysterious forest, with tall trees and "
                "the sound of rustling leaves all around.")
    print_pause("Legend has it that a hidden treasure is concealed somewhere "
                "in this forest, guarded by a fearsome creature.")
    print_pause("In your hand, you hold a worn-out map that marks the possible "
                "location of the treasure.")
    print_pause("Before you, there's a mysterious path leading deeper into the "
                "forest.")
    print_pause("To your right, you notice a peculiar-looking tree with an "
                "engraved symbol on its bark.")
    print_pause("What would you like to do?")

def forest_path():
    """
    Explore the forest path and encounter fairies.
    """
    print_pause("You decide to follow the path into the heart of the forest.")
    print_pause("The further you go, the darker and more mysterious it becomes.")
    print_pause("Suddenly, you encounter a group of mischievous fairies who block "
                "your way.")
    print_pause("They demand to know why you are in their territory.")

    choice2 = valid_input("Will you (1) try to befriend the fairies or (2) stand your "
                        "ground and demand passage?", ['1', '2'])
    if choice2 == "1":
        print_pause("You approach the fairies with a friendly demeanor and offer "
                    "them some shiny trinkets you found earlier.")
        print_pause("The fairies are pleased and grant you safe passage through "
                    "their forest.")
        print_pause("You continue on your quest, leaving the fairies behind.")
        cave(item, option)  # Pass the required arguments.
    elif choice2 == "2":
        print_pause("You stand your ground and insist on your right to pass.")
        print_pause("The fairies take offense and cast a spell on you, turning you "
                    "into a toad!")
        print_pause("Your adventure ends here, as you can't continue as a toad.")
        play_again()

# Create similar functions for enchanted_tree(), cave(), and treasure().

def play_again():
    """
    Restart or quit the game.
    """
    again = valid_input("Would you like to embark on another adventure? (y/n)", ['y', 'n'])
    if again == "y":
        print_pause("\n\n\nExcellent! Starting a new adventure...\n\n\n")
        play_game()
    elif again == "n":
        print_pause("\n\n\nThank you for playing! See you next time.\n\n\n")

def play_game():
    option = random.choice(["ancient guardian", "enigmatic spirit", "mystical "
                        "beast", "shadowy figure", "guardian of secrets"])
    intro()
    forest_path()

if __name__ == "__main__":
    play_game()
