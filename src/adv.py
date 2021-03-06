from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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
player = Player('Kenny', room["outside"])
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while True:
    print(f"\n{player.current_room.name}")
    print(f"{player.current_room.description} \n")

    selection = input("Choose which direction to move: ")

    if selection == "q":
        print("Thanks for playing!")
        break

    if player.current_room.name == room['outside'].name and selection == 'n':
        player.current_room = room['outside'].n_to
    elif player.current_room.name == room['foyer'].name and selection == 's':
        player.current_room = room['foyer'].s_to
    elif player.current_room.name == room['foyer'].name and selection == 'n':
        player.current_room = room['foyer'].n_to
    elif player.current_room.name == room['foyer'].name and selection == 'e':
        player.current_room = room['foyer'].e_to
    elif player.current_room.name == room['overlook'].name and selection == 's':
        player.current_room = room['overlook'].s_to
    elif player.current_room.name == room['narrow'].name and selection == 'w':
        player.current_room = room['narrow'].w_to
    elif player.current_room.name == room['narrow'].name and selection == 'n':
        player.current_room = room['narrow'].n_to
    elif player.current_room.name == room['treasure'].name and selection == 's':
        player.current_room = room['treasure'].s_to
    else:
        print('There is no room in that direction.')