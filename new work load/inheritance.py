class Dad:
    def football(self):
        print("Dad is not a fan of football.")

class Mom:
    def cooking(self):
        print("Mom is ok with cooking.")

class Son (Dad):
    def Son_age(self):
        print("He has a 3 year old son.")

my_son = Son()
my_son.football()
my_son.Son_age()

class Daughter (Mom):
    def Daughter_age(self):
        print("She has a 1 year old daughter.")

my_daughter = Daughter()
my_daughter.cooking()
my_daughter.Daughter_age()