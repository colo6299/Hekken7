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
        attack = random.choice(self.abilities)
        print(self.name + ': ' + attack.name)
        return attack.attack()

    
    def attack(self, enemy):
        if enemy.receive_attack(self.attack_value()):
            self.kills += 1


    def defence_value(self):
        defence_total = 0
        for armor in self.armors:
            defence_total += armor.block()
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
                print(self.name + ': NOOOOOOoooooo....')
                self.deaths += 1
                return True
            elif random.random() < self.encore_chance:
                print(self.name + ': NOT TODAY')
                self.current_health = self.starting_health // 2
                self.alive = True
            else:
                print(self.name + ': They got me...')
                self.deaths += 1
                return True
        return False

    
    def resurrect(self):
        self.current_health = self.starting_health
        self.kills = 0
        self.deaths = 0
        self.alive = True
            

class Sans(Hero):
    def __init__(self, name, starting_health=170, is_villain = False):
        self.counter = 0
        super().__init__(name, starting_health)

    def attack_value(self):
        attack = self.abilities[self.counter % len(self.abilities)]
        self.counter += 1
        print(self.name + ': ' + attack.name)
        return attack.attack()

    def attack(self, enemy):
        if self.attack_value() > 0:
            self.erase(enemy)

    def erase(self, enemy):
        enemy.encore_chance = 0
        enemy.current_health = 0
        enemy.starting_health = 0
        enemy.update_status()

        # Dissapear forever.
        enemy.alive = False
        self.kills += 1  


def hero_defaults():
    gink = Hero('Gink', 170)  # the legendary half-man, half-dog wrestling champ
    gink.abilities = [
        Ability('ROLLING DOG CRADLE!!!', 9999),
        Ability('FOOL! YOU PRESSED A BUTTON', 50),
        Ability('Hey, a jab\'s a jab...', 10),
        Ability('I\'LL STOMP YOUR FACE', 25)
    ]

    gink.armors = [
        Armor('Go ask armor gink', 0)
    ]


    glaudio = Hero('Glaudio', 170)  # The legendary italian farmer-turned-fighter
    glaudio.abilities = [
        Ability('SENTI IL MIO PODERE!!!', 9999),
        Ability('You call THAT a hopkick?', 50),
        Ability('Backhand!', 12),
        Ability('I have never seen a low in my life.', 2)
    ]

    glaudio.armors =[
        Armor('You flinched.', 5)
    ]


    regulardog = Hero('regulardog', 50)  # The legendary ...dog?
    regulardog.abilities = [
        Ability('ARF', 99),
        Ability('Woof!', 5),
        Ability('arf', 1)
    ]

    regulardog.armors =[
        Armor('fuzzzyyyyy :)', 5)
    ]


    superdog = Hero('SUPERDOG', 150)  # The legendary SUPERDOG
    superdog.abilities = [
        Ability('ARF', 9999),
        Ability('Woof!', 50),
        Ability('arf', 10)
    ]

    superdog.armors =[
        Armor('fuzzzyyyyy :)', 50)
    ]


    sans = Sans('sans', 500)  # doot doot doooot doot 
    sans.abilities = [
        Ability('It\'s a beautiful day outside.', 0),
        Ability('Birds are singing.', 0),
        Ability('Flowers are blooming.', 0),
        Ability('On days like these,', 0),
        Ability('kids like you...', 0),
        Ability('s h o u l d   b e   b u r n i n g   i n   h e l l.', 999999999999999999999999999999999999999999999999999999999999999999999999999999)
    ]

    sans.armors = [
        Armor('Pathetic.', 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
    ]


    regulardog = Hero('regulardog', 50)  # The legendary ...dog?
    regulardog.abilities = [
        Ability('ARF', 99),
        Ability('Woof!', 5),
        Ability('arf', 1)
    ]

    regulardog.armors =[
        Armor('fuzzzyyyyy :)', 5)
    ]
    

    return [gink, glaudio, regulardog, superdog, sans]


# Can we just, like, agree that this is enough to get me the 1 point in TDD?

def test_defaults():
    assert len(hero_defaults()) != 0  # there's stuff in the default roster


def test_hero():
    # checks that current health is set to starting health
    assert Hero('test', 120).current_health == 120

# test_hero()

