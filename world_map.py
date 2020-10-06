'''
This module creates the world map.
The map is a 4x4 matrix, with some dead ends.
Each room is a double-linked node with four directions: north, south, east and west. The player can go back or forward
in every room.
The player starts at the most northwest position and its objective is to reach the most southeast position to find the
treasure.
At the center of the grid, the player will find a boss.
'''

class Room:
    def __init__(self, content, north = None, south = None, east = None, west = None):
        self.content = content
        self.north = north
        self.south = south
        self.east = east
        self.west = west

class World:
    def ___init__(self, room):
        self.start = room

def build_world():
    world = World()

# Building rooms' contents
# Option: start/ potion/ empty/ strength up/ defense up/ miniboss/ boss/
    room1 = Room("start")
    room3 = Room("potion")
    room4 = Room("strength up")
    room5 = Room("defense up")
    room6 = Room("empty")
    room7 = Room("miniboss")
    room10 = Room("miniboss")
    room11 = Room("potion")
    room12 = Room("boss")
    room13 = Room("secret treasure")
    room14 = Room("potion")
    room16 = Room("end treasure")

# Linking rooms through directions fields
    room1.south = room5
    room3.south = room7
    room3.east = room4
    room4.west = room3
    room5.north = room1
    room5.east = room6
    room6.west = room5
    room6.east = room7
    room6.south = room10
    room7.west = room6
    room7.north = room3
    room7.south = room11
    room10.north = room6
    room10.east = room11
    room10.south = room14
    room11.west = room10
    room11.east = room12
    room11.north = room7
    room12.west = room11
    room12.south = room16
    room13.east = room14
    room14.west = room13
    room14.north = room10
    room16.north = room12

# Defining world start
    world.start = room1
    return world