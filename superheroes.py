import random


class Ability:
    def __init__(self, name, attack_strength):
        '''Create Instance Variables:
            name:String
            max_damage: Integer
        '''
        self.max_damage = attack_strength
        self.name = name


    def attack(self):
        ''' Return a value between 0 and the value set by self.max_damage.'''

        return random.randint(0, self.max_damage)


class Armor:
    def __init__(self, name, max_block):
        '''Instantiate instance properties.
            name: String
            max_block: Integer
        '''
        self.name = name
        self.max_block = max_block

    def block(self):
        return random.randint(0, self.max_block)


class Hero:
    def __init__(self, name, starting_health=170, is_villain = False):
        '''Instance properties:
            abilities: List
            armors: List
            name: String
            starting_health: Integer
            current_health: Integer
        '''
        self.starting_health = starting_health
        self.name = name
        self.is_villain = is_villain
        self.abilities = list()
        self.armors = list()

        self.current_health = starting_health
        self.encore_chance = 0.2
        self.alive = True

        self.kills = 0
        self.deaths = 0
        

    def add_ability(self, ability):
        self.abilities.append(ability)


    def add_armor(self, armor):
        self.armors.append(armor)


    def attack_value(self):
        attack_total = 0
        for ability in self.abilities:
            attack_total += ability.attack()
        return attack_total

    
    def attack(self, enemy):
        if enemy.receive_attack(self.attack_value()):
            self.kills += 1


    def defence_value(self):
        defence_total = 0
        for armor in self.armors:
            defence_total += armor.defend()
        return defence_total

    
    def receive_attack(self, damage):
        taken_damage = damage - self.defence_value()
        if taken_damage > 0:
            self.current_health -= taken_damage
        return self.update_status()
        

    def update_status(self):
        if self.current_health <= 0:
            self.alive = False
            if self.is_villain:
                print('NOOOOOOoooooo....')
                self.deaths += 1
                return True
            elif random.random < self.encore_chance:
                print('NOT TODAY')
                self.current_health = self.starting_health // 2
                self.alive = True
            else:
                print('They got me...')
                self.deaths += 1
                return True
        return False

    
    def resurrect(self):
        self.current_health = self.starting_health
        self.kills = 0
        self.deaths = 0
            

def hero_defaults():
    gink = Hero('Gink', 170)  # the legendary half-man, half-dog wrestling champ
    gink.add_ability(
        [
            Ability('ROLLING DOG CRADLE', 9999),
            Ability('YOU PRESSED A BUTTON', 50),
            Ability('JAB', 10),
            Ability('KICK', 15)
        ]
    )
    gink.add_armor(
        [
            Armor('Go ask armor gink instead', 0)
        ]
    )

    glaudio = Hero('Glaudio', 170)  # The legendary italian farmer-turned-fighter
    glaudio.add_ability(
        [
            Ability('SENTI IL MIO PODERE', 9999),
            Ability('YOU CALL THAT A HOPKICK?', 50),
            Ability('BACKHAND', 12),
            Ability('I HAVE NEVER SEEN A LOW IN MY LIFE', 2)
        ]
    )
    glaudio.add_armor(
        [
            Armor('You flinched.', 5)
        ]
    )

    return [gink, glaudio]






