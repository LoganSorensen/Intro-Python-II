# Write a class to hold player information, e.g. what room they are in
# currently.


class Player():
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def move_to(self, direction, current_room):
        attribute = direction + '_to'

        if hasattr(current_room, attribute):
            return getattr(current_room, attribute)

    def list_items(self):
        if len(self.inventory) == 0:
            return "Empty"
        else:
            for i in self.inventory:
                print(i.name)

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        self.inventory.remove(item)
