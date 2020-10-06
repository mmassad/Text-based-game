'''
This module defines the player and its data. The user must input a valid name and choose one job.
All jobs begin with 10 health points.

'''

class Player:
    def __init__(self, name = '', health = 10, strength = 5, defense = 5, potion = 0):
        self.name = name
        self.health = health
        self.strength = strength
        self.defense = defense
        self.potion = potion

class InvalidNameError(Exception):
    pass


def build_player():
    player = Player()
    whats_your_name(player)

    return player

def whats_your_name(player):
    try:
        player.name = input("What is your name? ")
        if not player.name.isalpha():
            raise InvalidNameError

    except InvalidNameError:
        print("Not a valid name, try again")
        whats_your_name(player)
