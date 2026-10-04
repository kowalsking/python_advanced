class Hero:

    
    def __init__(self, name: str):
        self.name = name
        self.hp = 100
        self.inventory = []
        
    def is_alive(self):
        print('is alive:', self.hp > 0)
        return self.hp > 0

    def take_damage(self, damage):
        if not self.is_alive(): return print('Hero is dead')
        self.hp -= damage
        print('dmg', self.hp)
        
    def heal(self, points):
        self.hp += points
        
    def add_item(self, item):
        self.inventory.append(item)
        
    def show_status(self):
        print(f'Name: {self.name}. Is alive: {self.is_alive()}. HP: {self.hp}. Inventory: {self.inventory}')
        
my_hero = Hero('Arthas')

my_hero.add_item('knife')
my_hero.take_damage(90)
my_hero.take_damage(90)
my_hero.take_damage(90)
my_hero.show_status()