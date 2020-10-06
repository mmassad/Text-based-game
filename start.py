import player
import world_map
import navigation
import fight

from navigation import AdventureEnded
from fight import DeadHero
''''
This module imports the player, world map and navigation modules.
The module is also responsible for starting, looping or stoping the game should the player 
make wrong decisions or have its health depleted.
'''

def start_world():
    print("Welcome, player!")
    p = player.build_player()
    w = world_map.build_world()
    main_loop(p, w)

def main_loop(player, world):
    try:
        navigation.print_texts(player, world)

    except AdventureEnded or DeadHero:

        if input(player.name + ", do you want to play again? (Y/N) ").lower() == "Y":
            start_world()
        else:
            print("Ok, see you", player.name, "!")
