import simplix
import superheroes
import team
import random


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


def teamfight(team_1: team.Team, team_2: team.Team):
    hero_1 = random.choice(team_1.heroes)
    hero_2 = random.choice(team_2.heroes) 
    
    duel(hero_1, hero_2)


def duel(hero_1, hero_2, to_the_death = False): # add no ABility tedsyrt

    kill_loop = False
    while (hero_1.alive and hero_2.alive) and not kill_loop:
        hero_1.attack(hero_2)
        hero_2.attack(hero_1)
        if not to_the_death:
            kill_loop = True

    if not hero_1.alive and not hero_2.alive:
        print("Both heroes have fallen!")
    elif hero_1.alive:
        print(hero_1.name + ' has beaten ' + hero_2.name)
    else:
        print(hero_2.name + ' has beaten ' + hero_1.name)



def loops_brother():
    
    roster = superheroes.hero_defaults()

    print('Please build Team 1...\n')
    team_1 = team.Team('Team 1', user_form_team(roster))

    print()

    print('Please build Team 2...\n')
    team_2 = team.Team('Team 2', user_form_team(roster))

    print('Would you like all duels to be to the death? y/n')
    user_in = simplix.user_word('', ['y', 'n'])
    if user_in == 'y':
        pass
    elif user_in == 'n':
        pass

    fight_loop = True
    while fight_loop:
        hero_1 = random.choice(team_1.heroes)
        hero_2 = random.choice(team_2.heroes) 
        duel(hero_1, hero_2)

        t1_dead = True
        for hero in team_1.heroes:
            if hero.alive:
                t1_dead = False

        t2_dead = True
        for hero in team_2.heroes:
            if hero.alive:
                t2_dead = False
        
        if t1_dead or t2_dead:
            print('\nThe fight is over,')
            if t1_dead and t2_dead:
                print('Both teams were eliminated!')
            elif t1_dead:
                print('Team 2 is victorious!')
            elif t2_dead:
                print('Team 1 is victorious!')
            team_1.call_for_stats()
            team_2.call_for_stats()
            
            print('Play again? y/n')
            user_in = simplix.user_word('', ['y', 'n'])
            if user_in == 'y':
                team_1.reset_team()
                team_2.reset_team()
            elif user_in == 'n':
                return

        input('\nEnter to continue...\n')

loops_brother()

