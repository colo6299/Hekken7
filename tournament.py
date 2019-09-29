import superheroes




def duel(hero_1, hero_2): # add no ABility tedsyrt

    while hero_1.is_alive and hero_2.is_alive:
        hero_1.attack(hero_2)
        hero_2.attack(hero_1)

    if not hero_1.is_alive and not hero_2.is_alive:
        print("Both heroes have fallen!")
    elif hero_1.is_alive:
        print(hero_1.name + ' has beaten ' + hero_2.name)
    else:
        print(hero_2.name + ' has beaten ' + hero_1.name)


