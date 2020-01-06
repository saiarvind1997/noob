"""
### Task_6 iterations


    def sleep(self):
        self.tmp= self.tmp - 200
        return "sleeping, total remaining calories in body is {}".format(self.tmp)  

    def move(self):
       self.tmp = self.tmp +100
       return "moving,total remainng calories in the body is {}".format(self.tmp)
    #def eat(self):
    #    self.tmp3=self.tmp + 1000
    #    return self.tmp

n=raw_input("\nDefine human names with commas\n").split(",")
h={name:Human(name=name,cal=2000) for name in n}
identity,action=raw_input("\nEnter name and desired state from sleep|eat|move|end\n").split()
print action
while action != "end":
    for i in h:
        h[i].tmp
        a={
            "sleep":h[i].sleep(),
            "move":h[i].move(),
            #"eat":h[i].eat()
            }    
        if identity==h[i].name:
            state=a[action]
            print state
            print "{} {} {}".format(h[i].name,h[i].tmp,h[i].cal)
            break
    else:             #else only activates when if reaches break. if it does not, the for loop keeps continuing with the if statment.
        print "RIP {}".format(identity)

    identity,action=raw_input("\nEnter your next move\n").split()
else:
    print("Destroy all humans")
identity,action=raw_input("\nEnter name and desired state from sleep|eat|move|end\n").split()
while action != "end":
    for i in n:
        h=Human(i,c)
        if identity==i and action=="sleep":
            print h.name
            print h.cal
            print h.sleep(200)
            print h.tmp
            c=h.tmp
            print h.cal
            break
        elif i==identity and action=="man":
            print a["man"]
            break
    identity,action=raw_input("\nEnter your next move\n").split()
########################################
n=raw_input("\nDefine human names with commas\n").split(",")  
h=Human(n)
print len(n)
print h.name

identity,action=raw_input("\nEnter name and desired state from sleep|eat|move|end\n").split()
print action

while action != "end":

    a={
    "status":h.status(),
    "sleep":h.sleep(),
    "eat":h.eat(),
    "move":h.move()
    }

    for x in h.name:
        if x==identity:
            state=a[action]
            print "{} is {}".format(x,state)
            break
    else:  #else only activates when if reaches break. if it does not, the for loop keeps continuing with the if statment.
        print "RIP {}".format(identity)

    identity,action=raw_input("\nEnter your next move\n").split()
else:
    print("Destroy all humans")

"""

