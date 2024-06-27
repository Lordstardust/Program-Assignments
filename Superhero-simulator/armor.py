# armor.py
import random

class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        return random.randint(0, self.max_block)

if __name__ == "__main__":
    armor = Armor("Shield", 20)
    print(armor.name)
    print(armor.block())
