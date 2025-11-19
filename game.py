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
    # only want to append if the item is not in the list
    if not item in player.inventory:
        player.inventory.append(item)          # - Adds the item to the inventory list
        print("You picked up", item + "!")   # - Prints a message saying the item was picked up

def explore_dark_woods(player):
    print(f"You go into the dark woods")
    add_to_inventory("lantern", player)
    player.has_lantern = True

def explore_mountain_pass(player):
    print("You got towards the mountain pass") # Concatenation example
    add_to_inventory("map", player)
    player.has_map = True

def explore_cave(player):
    if player.has_lantern:
        print("You go into the dark cave")
        add_to_inventory("treasure", player)
    else:
        print("It's too dark in the cave. Try to find something to illuminate your way")
        player.health -= 10

def explore_hidden_valley(player):
    if player.has_map:
        print("You go into the hidden valley with a bowl of salad")
        add_to_inventory("rare herbs", player)
    else:
        print("You can't find the valley without directions")
        player.health -= 10

def stay_still(player):
    print("Confused, you stand still, unsure of what to do.")
    player.health -= 10

def check_win(player):
    if "treasure" and "rare herbs" in player.inventory:
        print("You have won the game!")
        return True
    else:
        return False
    
def check_lost(player):
    if player.health <= 0:
        print("Your health has gone to 0. You die!")
        return True
    else:
        return False

player1 = welcome_player() #returns a player object
describe_area()

has_won = False

while (not has_won):
    # Ask the player for their first decision
    decision = input("\t1. Take the left path into the dark woods\n"
                    "\t2. Take the right path towards the mountain pass\n"
                    "\t3. Go into a nearby cave\n"
                    "\t4. Explore the hidden valley\n"
                    "\t5. Stay where you are \n"
                    "\tType 'i' to view your inventory ").lower()

    # conditional evaluate
    # Respond based on the player's decision
    if decision == "1": # = assignment operator == equivalent
        explore_dark_woods(player1)
    elif decision == "2":
        explore_mountain_pass(player1)
    elif decision == "3":
        explore_cave(player1)
    elif decision == "4":
        explore_hidden_valley(player1)
    elif decision == "5":
        stay_still(player1)
    elif decision == "i":
        print(player1.inventory)
    else:
        print("That is not a valid choice")
    
    print("Your health is:", player1.health)
    has_lost = check_lost(player1)
    if has_lost:
        break
    has_won = check_win(player1)