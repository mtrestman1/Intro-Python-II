# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Item

class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.inventory = [
            Item("13in laptop", "how do you even code on that")
        ]



