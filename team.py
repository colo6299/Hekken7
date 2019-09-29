class Team:

    def __init__(self, team_name = 'Nobodies', heroes = []):
        self.heroes = heroes
        self.name = team_name

        self.wins = 0
        self.losses = 0
        self.kills = 0
        self.deaths = 0
    
    
    def add_hero(self, hero):
        self.heroes.append(hero)

    
    def remove_hero(self, hero_to_remove):
        self.heroes.remove(hero_to_remove)

    
    def agg_stats(self):
        self.kills = 0
        self.deaths = 0
        for hero in self.heroes:
            self.kills += hero.kills
            self.deaths += hero.deaths

    
    def report_stats(self):
        print(f'Team {self.name} K/DR: {self.kills/self.deaths}')
                
        
    def call_for_stats(self):
        self.agg_stats()
        self.report_stats()

    
    def resurrect(self):
        for hero in self.heroes:
            hero.resurrect()