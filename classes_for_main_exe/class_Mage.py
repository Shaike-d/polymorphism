import classes_for_main_exe.class_Character as c
class Mage(c.Character):


    def __init__(self,name,health):
        super().__init__(name,health)

    def attack_power(self):

        if self.health <= 50:
            return 10
        else: 
            return 20