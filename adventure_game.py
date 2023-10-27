import time
import random

def print_pause(msg_to_print):
    print(msg_to_print)
    time.sleep(2)

def intro(item, option):
    print_pause("You find yourself in a mysterious forest, with tall trees and"
                " the sound of rustling leaves all around.\n")
    print_pause("Legend has it that a hidden treasure is concealed somewhere "
                "in this forest, guarded by a fearsome creature.\n")
    print_pause("In your hand, you hold a worn-out map that marks the possible "
                "location of the treasure.\n")
    print_pause("Before you, there's a mysterious path leading deeper into the "
                "forest.\n")
    print_pause("To your right, you notice a peculiar-looking tree with an "
                "engraved symbol on its bark.\n")
    print_pause("What would you like to do?\n")

def forest_path(item, option):
    print_pause("You decide to follow the path into the heart of the forest.")
    print_pause("The further you go, the darker and more mysterious it becomes.")
    print_pause("Suddenly, you encounter a group of mischievous fairies who block "
                "your way.\n")
    print_pause("They demand to know why you are in their territory.")
    while True:
        choice2 = input("Will you (1) try to befriend the fairies or (2) stand your "
                        "ground and demand passage?\n")
        if choice2 == "1":
            print_pause("You approach the fairies with a friendly demeanor and offer "
                        "them some shiny trinkets you found earlier.")
            print_pause("The fairies are pleased and grant you safe passage through "
                        "their forest.")
            print_pause("You continue on your quest, leaving the fairies behind.\n")
            cave(item, option)
            break
        elif choice2 == "2":
            print_pause("You stand your ground and insist on your right to pass.")
            print_pause("The fairies take offense and cast a spell on you, turning you "
                        "into a toad!")
            print_pause("Your adventure ends here, as you can't continue as a toad.\n")
            play_again()
            break

def enchanted_tree(item, option):
    print_pause("You decide to inspect the peculiar tree with the engraved symbol.")
    print_pause("As you approach, the symbol on the tree begins to glow, and "
                "the tree comes to life.")
    print_pause("The tree speaks and offers to share its ancient wisdom with you.")
    while True:
        choice3 = input("Will you (1) accept the tree's wisdom or (2) decline the offer "
                        "and continue on your quest?\n")
        if choice3 == "1":
            print_pause("You accept the tree's wisdom and learn valuable insights about "
                        "the forest and the treasure's location.")
            print_pause("Thanking the enchanted tree, you move forward with newfound "
                        "knowledge.\n")
            cave(item, option)
            break
        elif choice3 == "2":
            print_pause("You politely decline the tree's offer and continue on your path.")
            print_pause("The tree nods and watches as you disappear into the forest.\n")
            cave(item, option)
            break

def cave(item, option):
    print_pause("You arrive at a dark and mysterious cave, as marked on your map.")
    print_pause("It's said that the treasure might be hidden deep within.")
    print_pause("As you venture further into the cave, you encounter a sleeping dragon!")
    if "sword" in item:
        print_pause("Fortunately, you already have a magical sword, which gives you "
                    "confidence.")
        while True:
            choice4 = input("Will you (1) sneak past the dragon or (2) attempt to "
                            "defeat it with your sword?\n")
            if choice4 == "1":
                print_pause("You carefully sneak past the dragon without waking it, "
                            "continuing deeper into the cave.")
                treasure(item, option)
                break
            elif choice4 == "2":
                print_pause("You muster your courage, unsheath your magical sword, and "
                            "engage the dragon in a fierce battle.")
                print_pause("After a mighty struggle, you defeat the dragon and continue "
                            "your quest.")
                treasure(item, option)
                break
    else:
        print_pause("You feel unprepared to face the dragon with your current equipment.")
        print_pause("You decide to quietly retreat from the cave to find a better "
                    "weapon.")
        print_pause("Back outside, you ponder your next move.\n")
        forest_path(item, option)

def treasure(item, option):
    print_pause("As you venture deeper into the cave, you stumble upon a hidden chamber.")
    print_pause("In the chamber, you find a magnificent chest, and inside it lies the "
                "legendary treasure!")
    print_pause("Congratulations! You've successfully found the hidden treasure.")
    print_pause("You are hailed as a hero and return home with the treasure, which "
                "brings prosperity to your village.")
    print_pause("You have completed your quest and achieved great success!\n")
    play_again()

def play_again():
    again = input("Would you like to embark on another adventure? (y/n) ").lower()
    if again == "y":
        print_pause("\n\n\nExcellent! Starting a new adventure...\n\n\n")
        play_game()
    elif again == "n":
        print_pause("\n\n\nThank you for playing! See you next time.\n\n\n")
    else:
        play_again()

def play_game():
    item = []
    option = random.choice(["ancient guardian", "enigmatic spirit", "mystical "
                            "beast", "shadowy figure", "guardian of secrets"])
    intro(item, option)
    forest_path(item, option)

play_game()
