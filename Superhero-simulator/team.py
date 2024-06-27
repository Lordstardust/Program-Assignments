# team.py
class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = []

    def add_hero(self, hero):
        self.heroes.append(hero)

    def remove_hero(self, name):
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                return

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

if __name__ == "__main__":
    from hero import Hero

    team = Team("Avengers")
    hero1 = Hero("Iron Man")
    hero2 = Hero("Thor")
    team.add_hero(hero1)
    team.add_hero(hero2)
    team.view_all_heroes()
# team.py (updated)
class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = []
        self.total_kills = 0
        self.total_deaths = 0

    def add_hero(self, hero):
        self.heroes.append(hero)

    def remove_hero(self, name):
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                return

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

    def attack(self, other_team):
        while any(hero.is_alive() for hero in self.heroes) and any(hero.is_alive() for hero in other_team.heroes):
            hero1 = random.choice([hero for hero in self.heroes if hero.is_alive()])
            hero2 = random.choice([hero for hero in other_team.heroes if hero.is_alive()])
            hero1.battle(hero2)
            if hero1.is_alive():
                hero1.add_kill(1)
                other_team.total_deaths += 1
            else:
                hero2.add_kill(1)
                self.total_deaths += 1

    def revive_heroes(self):
        for hero in self.heroes:
            hero.current_health = hero.starting_health
