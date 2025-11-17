class Player():
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.health = 100
        self.has_map = False
        self.has_lantern = False


# TODO: Create a class called Player to represent the player in the game

# TODO: Inside the Player class, define an __init__ method that:
#       - Takes a name parameter
#       - Initializes these attributes:
#         - self.name (string)
#         - self.inventory (empty list)
#         - self.health (set to 100)
#         - self.has_map (set to False)
#         - self.has_lantern (set to False)