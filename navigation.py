'''
This module presents the texts to the player. Each text is built based on the contents of the room and its possible
navigation directions, defined on the module world_map
'''
import player
import world_map
import fight

class InvalidDirection(Exception):
    pass
class AdventureEnded(Exception):
    pass

def print_texts(player, world):
    current_room = world.start

    while current_room:
        print_room_content(player, current_room)
        current_room = choose_next_room(current_room)

def print_room_content(player, room):
    if room.content == "start":
        print(player.name + ' , you are at the start of the dungeon.')
    elif room.content == "potion":
        print('You found a potion.')
        player.potion += 1
        room.content = "empty"

    elif room.content == "strength up":
        print('You found the legendary sword! Your strength has increased by 3 points.')
        player.strength += 3
        room.content = "empty"

    elif room.content == "defense up":
        print('You can see an abandoned shield on the floor. Your defense has increased by 2 points.')
        player.defense += 2
        room.content = "empty"

    elif room.content == "miniboss":
        print('As you entered the room, a goblin appeared!')
        fight.fight(player, "miniboss")
        room.content = "defeated miniboss"

    elif room.content == "boss":
        print('As soon as you open the golden door, you hear a trembling roar. A golden dragon awakens from his sleep!')
        fight.fight(player, "boss")
        room.content = "defeated boss"

    elif room.content == "secret treasure":
        print('You have found the secret treasure! Congratulations, '+ player.name + " !")

    elif room.content == "end treasure":
        print('At last, you found what you were looking for... The scroll of truth!')
        raise AdventureEnded

    elif room.content == "empty":
        print('There doesn''t seem to be anything of interest in this room.')

    elif room.content == "defeated miniboss":
        print('The defeated goblin lies on the floor.')

    elif room.content == 'defeated boss':
        print("The once majestic dragon is on its resting place.")

def choose_next_room(room):
    try:
        index = 1
        str_options = ""
        print('\nWhere would you like to go?')
        if room.north:
            str_options += str(index)+" - Go north (N) \t"
            index += 1
        if room.south:
            str_options += str(index)+" - Go south (S) \t"
            index += 1
        if room.east:
            str_options += str(index)+" - Go east (E) \t"
            index += 1
        if room.west:
            str_options += str(index)+" - Go west (W)"

        print(str_options)
        ans = input('Type the chosen character: \t').upper()
        print("\n")

        if ans == 'N' and room.north:
            return room.north
        elif ans == 'S' and room.south:
            return room.south
        elif ans == 'E' and room.east:
            return room.east
        elif ans == 'W' and room.west:
            return room.west
        else:
            raise InvalidDirection


    except InvalidDirection:
        print("Please type a valid character (N/S/E/W)")
        return choose_next_room(room)