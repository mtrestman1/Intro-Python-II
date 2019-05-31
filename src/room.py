# Implement a class to hold room information. This should have name and
# description attributes.

from item import Item

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = [
            Item("candle", "it gets dark at night"),
            Item("sock", "smells bad but keeps the feet warm"),
            Item("some food item", "always hungry")
        ]

    