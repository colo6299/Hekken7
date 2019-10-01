import simplix
import superheroes
import team


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


def user_form_team(default_heroes):  
    # All my code is IP68 rated, this should be fine.

    new_team_list = []

    print('The heroes currently available are:')
    for hero in default_heroes:
        print('  * ' + hero.name)
    print('Please enter a name, or enter \'done\' to finish:')

    valid_inputs = ['done']
    for hero in default_heroes:
        valid_inputs.append(hero.name.lower())

    started = False
    finish_team = False
    while not finish_team:
        if started:
            print('This is the current team roster:')

            for hero in new_team_list:
                print('  * ' + hero.name)
            print('\nAnyone else, or are you done?')

        user_in = simplix.user_word(words_to_match=valid_inputs)
        if user_in == 'done' and len(new_team_list) == 0:
            print('Teams cannot be empty.')
        elif user_in == 'done':
            finish_team = True
        else:
            for hero in default_heroes:
                if hero.name.lower() == user_in:
                    new_team_list.append(hero)
        print()
        started = True
    return new_team_list

    def loops_brother():
        
        roster = superheroes.hero_defaults()

        input('Please build Team 1...\n')
        team_1 = team.Team('Team 1', user_form_team(roster))

        input('Please build Team 2...\n')
        team_2 = team.Team('Team 2', user_form_team(roster))
    
