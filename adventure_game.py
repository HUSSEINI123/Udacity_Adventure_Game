import time
import random

def print_pause(msg):
    print(msg)
    time.sleep(2)

def valid_input(prompt, options):
    while True:
        response = input(prompt).lower()
        if response in options:
            return response
        print("Invalid input!")

def intro():
    print_pause("You're in a mysterious forest, seeking hidden treasure.")
    print_pause("In your hand, a worn-out map marks its possible location.")
    print_pause("Before you, a path leads deeper into the forest.")
    print_pause("To your right, a tree with an engraved symbol awaits.")
    print_pause("What will you do?")

def encounter(item, opponent, scenario):
    print_pause(scenario)
    choice = valid_input("Will you (1) or (2)? ", ['1', '2'])
    return choice

def play_game():
    item = []
    opponent = random.choice(["ancient guardian", "enigmatic spirit", "mystical beast", "shadowy figure", "guardian of secrets"])
    intro()

    choice = encounter(item, opponent, "You follow the path into the forest and encounter mischievous fairies blocking your way.\nThey demand to know why you're here. Will you (1) befriend them or (2) stand your ground?")
    
    if choice == "1":
        print_pause("You befriend the fairies, who grant you safe passage. You continue on your quest.")
        choice = encounter(item, opponent, "You reach a mysterious cave, said to house the treasure. As you venture further, you encounter a sleeping dragon. Will you (1) sneak past or (2) engage with your sword?")
        
        if choice == "1":
            print_pause("You sneak past the dragon and find the treasure!")
        elif choice == "2":
            if "sword" in item:
                print_pause("You use your magical sword to defeat the dragon and find the treasure!")
            else:
                print_pause("You lack the necessary equipment to defeat the dragon. You retreat.")
                play_again()
    elif choice == "2":
        print_pause("The fairies cast a spell, turning you into a toad. Your adventure ends here.")
        play_again()

    play_again()

def play_again():
    again = valid_input("Play again? (y/n) ", ['y', 'n'])
    if again == "y":
        print_pause("Starting a new adventure...")
        play_game()
    elif again == "n":
        print_pause("Thanks for playing! See you next time.")

if __name__ == "__main__":
    play_game()
