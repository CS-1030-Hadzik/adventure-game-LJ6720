"""
Adventure Game
Author: Logan Johnson
Version: 1.0
Description:
This is a text-based adventure game where the player makes choices
to navigate through a mysterious forest.
"""
from Player import Player

def welcome_player():
    # Welcome message and introduction
    print("Welcome to the Adventure Game!")
    print("Your journey begins here...")

    # Ask for the player's name
    player_name = input("What is your name, adventurer? ")

    # Use an f-string to display the same message in a more readable way
    print(f"Welcome, {player_name}! Your journey begins now.")

    player = Player(player_name)

    return player

def describe_area():
    # Describe the starting area
    starting_area = """
    You find yourself in a dark forest...
    You see two paths ahead:
    """
    print(starting_area)

def add_to_inventory(item, player):         # - Takes an item (string) as a parameter
    player.inventory.append(item)          # - Adds the item to the inventory list
    print("You picked up", item + "!")   # - Prints a message saying the item was picked up

player1 = welcome_player() #returns a player object
describe_area()


while (True):
    # Ask the player for their first decision
    decision = input("\t1. Take the left path into the dark woods\n"
                    "\t2. Take the right path towards the mountain pass\n"
                    "\t3. Stay where you are \n"
                    "\tType 'i' to view your inventory ").lower()

    # conditional evaluate
    # Respond based on the player's decision
    if decision == "1": # = assignment operator == equivalent
        print(f"You go into the dark woods")
        add_to_inventory("lantern", player1)
        player1.has_lantern = True
    elif decision == "2":
        print("You got towards the mountain pass") # Concatenation example
        add_to_inventory("map", player1)
        player1.has_map = True
    elif decision == "3":
        print("Confused, you stand still, unsure of what to do.")
    elif decision == "i":
        print(player1.inventory)
    else:
        print("That is not a valid choice")