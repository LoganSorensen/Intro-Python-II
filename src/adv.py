from room import Room
from player import Player
from item import Item


item = {
    'book': Item('book', "The cover reads, 'Goodnight Moon'."),
    'sword': Item('sword', "You grabbed it by the blade for some reason..."),
    'rock': Item('rock', "I mean, I guess you can have it if you really want it."),
    'hat': Item('hat', "It's a yankee with no brim!"),
    'coins': Item('coins', "Hang on, didn't the room description say that there was no treasure? Where on earth are you getting these?"),
}

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", item['book']),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", item['sword']),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", item['hat']),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", item['rock']),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", item['coins']),
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


def help_text():
    print("""
    Valid commands:
    -[n]: move north
    -[s]: move south
    -[e]: move east
    -[w]: move west
    -[i/inventory]: check inventory
    -[q]: quit game
    -[help/?]: help
    """)


def room_text():
    print(f"\n{player.current_room.name}")
    print(f"{player.current_room.description} \n")


room_text()


while True:

    selection = input("Enter a command: ")

    inputs = selection.split(maxsplit=1)

    if len(inputs) == 1:
        if selection == "q":
            print("Thanks for playing!")
            break

        if selection in ['?', 'help']:
            help_text()

        if selection in ['n', 's', 'e', 'w']:
            # if player.current_room.n_to == None or player.current_room.s_to == None or player.current_room.e_to == None or player.current_room.w_to == None:
            #     print("\nYou can't move in that direction\n")
            #     continue
            # else:
            if player.move_to(selection, player.current_room) == None:
                print("\nThere's nothing in that direction\n")
            else:
                player.current_room = player.move_to(
                    selection, player.current_room)
                room_text()
            # print(player.current_room.items)
            continue
        if selection in ['i', 'inv', 'inventory']:
            player.list_items()
            # print(f"\nInventory: {player.list_items()}\n")

        if selection == 'look':
            # for i in player.current_room.items:
            #     print(i.name)
            if len(player.current_room.items) == 0:
                print("\nYou don't see anything of use.\n")

            else:
                for i in player.current_room.items:
                    print(f"\nLooking around, you see a {i.name}.\n")

    elif len(inputs) == 2:
        action, obj = inputs[0], inputs[1]
        if action in ['get', 'take']:
            for i in player.current_room.items:
                if obj in i.name:
                    player.current_room.remove_item(i)
                    item[obj].on_take(i)
                    player.add_item(i)
                else:
                    print("\nThat item doesn't exist.\n")
        if action in ['drop']:
            for i in player.inventory:
                # print(i.name)
                if obj in i.name:
                    player.remove_item(i)
                    item[obj].on_drop(i)
                    player.current_room.add_item(i)
                else:
                    print("You don't have that item in your inventory.")


    # if player.current_room.name == room['outside'].name and selection == 'n':
    #     player.current_room = room['outside'].n_to
    # elif player.current_room.name == room['foyer'].name and selection == 's':
    #     player.current_room = room['foyer'].s_to
    # elif player.current_room.name == room['foyer'].name and selection == 'n':
    #     player.current_room = room['foyer'].n_to
    # elif player.current_room.name == room['foyer'].name and selection == 'e':
    #     player.current_room = room['foyer'].e_to
    # elif player.current_room.name == room['overlook'].name and selection == 's':
    #     player.current_room = room['overlook'].s_to
    # elif player.current_room.name == room['narrow'].name and selection == 'w':
    #     player.current_room = room['narrow'].w_to
    # elif player.current_room.name == room['narrow'].name and selection == 'n':
    #     player.current_room = room['narrow'].n_to
    # elif player.current_room.name == room['treasure'].name and selection == 's':
    #     player.current_room = room['treasure'].s_to
    # else:
    #     print('There is no room in that direction.')
