from room import Room
from player import Player
from item import Item

#  Declare all items
items = {
    "coins": Item("coins",
                  "Some coins that you can buy more stuff"),
    "sword": Item("sword",
                  "It does what a sword does."),
    "hammer": Item("hammer", "It chops things."),
    "gun": Item("gun", "It shoots."),
    "arrow": Item("arrow", "With a bow, it does everything")
}

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [items["coins"]]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [items["sword"]]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [items["hammer"]]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [items["gun"]]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [items["arrow"]]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player_name = input("Enter character name: ")
player = Player(player_name, room["outside"])
# Write a loop that:

while True:
    # * Prints the current room name

    # * Prints the current description (the textwrap module might be useful here).
    # print(room[player.current_room])
    print(f"{player.room}, Description:{player.room.description}, Items in room:{player.room.items}")
    print(f"Your Inventory: {player.inventory}")
    # print all the items
    # for item in {player.room}:
    #     print(f"Item:{item.name}, Description:{item.description}")

# * Waits for user input and decides what to do.
    player_input = input("Enter your next move: ")
    print(len(player_input))
# If the user enters a cardinal direction, attempt to move to the room there.

    if len(player_input) == 1:
        try:
            if player_input == "n":
                player.room = player.room.n_to
            elif player_input == "s":
                player.room = player.room.s_to
            elif player_input == "e":
                player.room = player.room.e_to
            elif player_input == "w":
                player.room = player.room.w_to
            elif player_input == "q":
                print("You have left the game. Thank you for playing.")
                break
        except:
            print("Wrong move! Try again.")

    if len(player_input) >= 2:
        print(f'get {item.name}')
        try:
            if player_input == f"get {item.name}":
                player.add_item(item)
                print(f"{item.name} added to your inventory")
            elif player_input.contain("drop"):
                player.drop_item(item)
                print(f"{player_input[1]} removed from your inventory")
        except:
            print("Invalid Action! Try again.")


else:
    print("Who's the player?")
# Print an error message if the movement isn't allowed.


# If the user enters "q", quit the game.
