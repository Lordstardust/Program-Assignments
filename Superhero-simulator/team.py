# team.py
from hero import Hero

class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = []

    def add_hero(self, hero):
        self.heroes.append(hero)

    def remove_hero(self, name):
        found_hero = False
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                found_hero = True
        return found_hero

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

if __name__ == "__main__":
    team = Team("Avengers")
    hero1 = Hero("Iron Man")
    hero2 = Hero("Thor")
    team.add_hero(hero1)
    team.add_hero(hero2)
    team.view_all_heroes()
