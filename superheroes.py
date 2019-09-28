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
        

    def add_ability(self, ability):
        self.abilities.append(ability)


    def add_armor(self, armor):
        self.armors.append(armor)


    def attack(self):
        attack_total = 0
        for ability in self.abilities:
            attack_total += ability.attack()
        return attack_total


    def defend(self):
        defence_total = 0
        for armor in self.armors:
            defence_total += armor.defend()
        return defence_total

    
    def take_damage(self, damage):
        taken_damage = damage - self.defend()
        if taken_damage > 0:
            self.current_health -= taken_damage
        

    def update_status(self):
        if self.current_health <= 0:
            self.alive = False
            if self.is_villain:
                print('NOOOOOOOOOOOO!')
            elif random.value < self.encore_chance:
                print('NOT TODAY')
                self.current_health = self.starting_health // 2
                self.alive = True
            

            



