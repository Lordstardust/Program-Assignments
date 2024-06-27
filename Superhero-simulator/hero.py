# hero.py
class Hero:
    
    def __init__(self, name, starting_health=100):
        '''Instance properties:
          name: String
          starting_health: Integer

          current_health: Integer
        '''
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    my_hero = Hero("Grace Hopper", 200)
    print(my_hero.name)
    print(my_hero.current_health)
# hero.py
class Hero:
    
    def __init__(self, name, starting_health=100):
        '''Instance properties:
          name: String
          starting_health: Integer

          current_health: Integer
        '''
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    my_hero = Hero("Grace Hopper", 200)
    print(my_hero.name)
    print(my_hero.current_health)
# hero.py (updated)
class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = []
        self.armors = []

    def add_ability(self, ability):
        self.abilities.append(ability)

    def add_armor(self, armor):
        self.armors.append(armor)

    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def defend(self):
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return total_block

    def take_damage(self, damage):
        defense = self.defend()
        damage_taken = damage - defense
        self.current_health -= damage_taken

    def is_alive(self):
        return self.current_health > 0

    def battle(self, opponent):
        if not self.abilities and not opponent.abilities:
            print("Draw")
            return
        while self.is_alive() and opponent.is_alive():
            opponent.take_damage(self.attack())
            if opponent.is_alive():
                self.take_damage(opponent.attack())
        if self.is_alive():
            print(f"{self.name} won!")
        else:
            print(f"{opponent.name} won!")

if __name__ == "__main__":
    from ability import Ability
    from armor import Armor

    hero1 = Hero("Hero One")
    hero2 = Hero("Hero Two")
    hero1.add_ability(Ability("Punch", 50))
    hero1.add_armor(Armor("Shield", 20))
    hero2.add_ability(Ability("Kick", 45))
    hero1.battle(hero2)

class Hero:
    

    def add_weapon(self, weapon):
        self.abilities.append(weapon)

if __name__ == "__main__":
    from weapon import Weapon

    hero1 = Hero("Hero One")
    hero1.add_weapon(Weapon("Sword", 100))
    print(hero1.attack())

class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = []
        self.armors = []
        self.deaths = 0
        self.kills = 0

    def add_kill(self, num_kills):
        self.kills += num_kills

    def add_death(self, num_deaths):
        self.deaths += num_deaths
