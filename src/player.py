# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.inventory = []

    def __str__(self):
        return f"Player:{self.name}"

    # def __repr__(self):
    #     return f"Player({repr(self.name, self.room)})"

    def add_item(self, item):
        if item in self.room.items:
            self.room.items.remove(item)
            self.inventory.append(item)
            print(f"Added {item.name} to inventory.")
        else:
            print("You got nothing.")

    def drop_item(self, item):
        if item in self.items:
            self.inventory.remove(item)
            self.room.items.append(item)
            print(f"{item.name} removed from your inventory.")

    def view_inventory(self):
        if len(self.inventory) > 0:
            for i in self.inventory:
                print(i.name)
        else:
            print("There is nothing in your inventory now")
