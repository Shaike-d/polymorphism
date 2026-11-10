class Character:

    def __init__(self,name,health):
        self.name = name
        self.health = health

    def attack_power(self):
        raise NotImplementedError('')




def attack(warrior,mage):
    mage.health -= warrior.attack_power()
    print(f"{warrior.name} hits {mage.name} for {warrior.attack_power()}")