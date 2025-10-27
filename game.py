"""
Adventure Game
Author: Logan Johnson
Version: 1.0
Description:
This is a text-based adventure game where the player makes choices
to navigate through a mysterious forest.
"""

# TODO: Define a function called add_to_inventory(item) that:
#       - Takes an item (string) as a parameter
#       - Adds the item to the inventory list
#       - Prints a message saying the item was picked up

def welcome_player():
    # Welcome message and introduction
    print("Welcome to the Adventure Game!")
    print("Your journey begins here...")

    # Ask for the player's name
    player_name = input("What is your name, adventurer? ")

    # Use an f-string to display the same message in a more readable way
    print(f"Welcome, {player_name}! Your journey begins now.")

    return player_name

def describe_area():
    # Describe the starting area
    starting_area = """
    You find yourself in a dark forest.
    The sound of rustling leaves fills the air.
    A faint path lies ahead, leading deeper into the unknown...
    """
    print(starting_area)

name = welcome_player()
describe_area()

# Ask the player for their first decision
decision = input("Do you wish to take the path? (yes or no): ").lower()

# conditional evaluate
# Respond based on the player's decision
if decision == "yes": # = assignment operator == equivalentLo
    print(f"Brave choice, {name}! You step onto the path and venture forward.")
elif decision == "no":
    print(name + ", you decide to wait. Perhaps courage will find you later.") # Concatenation example
else:
    print("Confused, you stand still, unsure of what to do.")