from player import Player
# Implement a class to hold room information. This should have name and
# description attributes.


class Room():
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = [items]

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            # print('if is firing')
        else:
            # print('else is firing')
            return None

    def add_item(self, item):
        # print("dropped item", item)
        self.items.append(item)
            