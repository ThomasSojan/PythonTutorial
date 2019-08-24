import random

#simple random value generation

for i in range(3):
    x = random.random()
    print(x)
#generate number btw 1 and 6 using randint method
class Die:
    def roll(self):
        roll1 = random.randint(1,6)
        roll2 = random.randint(1,6)
        roll3= random.randint(1,6)
        roll4 = random.randint(1,6)
        return(roll1,roll2,roll3,roll4)    

die = Die()
output = die.roll()    
print(output)    

#random selection using choice method

names = ["thomas","tom","aswin","hgovind","georgey","jake"]

leader = random.choice(names)
print(leader)