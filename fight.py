class DeadHero(Exception):
    pass

def fight (player, opponent):
    if opponent == "miniboss":
        print("Fighting goblin")

    if opponent == "boss":
        print("Fighting dragon")