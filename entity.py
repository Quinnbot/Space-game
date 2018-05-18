from inventory import inventory
from stats import stats

class entity(inventory):
    def __init__(self, name, stat):
        super().__init__()
        self.name = name
        self.stat = stats(stat[0], stat[1], stat[2], stat[3])

    def Name(self):
        return self.name

    def stats(self, choice):
        """
        0 = strength
        1 = agility
        2 = charisma
        3 = health
        """
        if(choice == 0):
            return self.stat.Strength(0,0)
        if(choice == 1):
            return self.stat.Agility(0,0)
        if(choice == 2):
            return self.stat.Charisma(0,0)
        if(choice == 3):
            return self.stat.Health(0,0)

    def changeStats(self, choice, val):

        if(choice == 0):
            return self.stat.Strength(1, val)
        if(choice == 1):
            return self.stat.Agility(1, val)
        if(choice == 2):
            return self.stat.Charisma(1, val)
        if(choice == 3):
            return self.stat.health(1, val)
