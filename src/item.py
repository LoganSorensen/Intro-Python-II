class Item():
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self, item):
        print(f"\nYou have picked up the {item}!\n")

    def on_drop(self, item):
        print(f"\nYou dropped the {item}.\n")