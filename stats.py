"""
modes
0 = return
1 = set
"""
class stats(object):

    def __init__(self, strength, agility, charisma, health):
        self.strength = strength
        self.agility = agility #remember to use self alot
        self.charisma = charisma
        self.health = health

    def Strength(self, choice, val):
        if(choice == 0):
            return self.strength
        if(choice == 1):
            self.strength = val
            return self.strength

    def Agility(self, choice, val):
        if(choice == 0):
            return self.agility
        if(choice == 1):
            self.agility = val
            return self.agility

    def Charisma(self, choice, val):
        if(choice == 0):
            return self.charisma
        if(choice == 1):
            self.charisma = val
            return self.charisma

    def Health(self, choice, val):
        if(choice == 0):
            return self.health
        if(choice == 1):
            self.health = val
            return self.health
