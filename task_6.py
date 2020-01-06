class Human:
    def __init__(self,name,cal):
        self.name=name
        self.cal=cal
        #self.tmp=self.cal
    def sleep(self):
        self.cal = self.cal - 200 
        return "{} is sleeping, total remaining calories in body is {}".format(self.name,self.cal)
    def move(self):
        self.cal = self.cal - 100
        return "{} is moving, total remaining calories in body is {}".format(self.name,self.cal)
    def eat(self):
        self.cal = self.cal + 1000
        return "{} is eating, total remaining calories in body is {}".format(self.name,self.cal)
        #self.tmp = self.cal - 100
        #self.cal=self.tmp
c=2000
n=raw_input("\nDefine human names with commas\n").split(",")
h={name:Human(name=name,cal=c) for name in n}
#print h
identity,action=raw_input("\nEnter name and desired state from sleep|eat|move|end\n").split()
while action!="end":
    for i in n:
        if i==identity:
            if action=="sleep":
                print h[i].sleep()
            elif action=="move":
                print h[i].move()
            elif action=="eat":
                print h[i].eat()
            else:
                print "action denied, enter 'exit' to end to die/n"
            break    
    else:
        print "Human still in womb"
    identity,action=raw_input("\nEnter name and desired state from sleep|eat|move|end\n").split()










    
















"""#Task 6
create a human class
give it functions, move, sleep, eat
give it class variables calories
sleeping burns 200 cals
moving burns 200 cals
eating adds 1000 cals
it should take input from command line
example 
step 1 should print 
create your humans
>sai, arvind, shariq
then I will entry a human <name> <action>
if I type "arvind eat" it should print "ate meals, total remaining calories in body is ____"
and then it should print "enter your next move"
"""