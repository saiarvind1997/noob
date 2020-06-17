import requests
### try making a inhereted class called sex class sex:
class Human:
    def __init__(self,name,cal):
        self.name=name
        self.cal=cal
class gender(Human):
    def __init__(self,):




"""
url="https://randomuser.me/api/"
#n=raw_input("\nDefine human names with commas\n").split(",")
#g=raw_input("\nDefine human genders of the following names with commas\n").split(",")
i=0
m=[]
f=[]
#h=Human("sai","female")
#h1=Human("ivy","female")
#print h.sex(h.gender,h1.gender)
population=True
while population:
    n=raw_input("\nDefine human name and gender with commans and enter 'end,spawn' to end spawing of humans\n").split(",")
    try:
        if n[1]=="Male" or n[1]=="male":
            m.append(n[0])
        elif n[1]=="Female" or n[1]=="female" :
            f.append(n[0])
        elif n[0]=="end" and  n[1]=="spawn":
            population=False
    except:
        print "gender not defined"
    print m
    print f
male={name:Human(name=name,gender="Male") for name in m}
female={name:Human(name=name,gender="Female") for name in f}
print male
print female

identity,identity2,action=raw_input("\nEnter a male,female and desired state from sleep|eat|move|sex|end\n").split()
while action!="end":
    for i in male:
        for j in female:
            if (identity==i and identity2==j) or (identity2==i and identity==j):# try more
                print i
                print j
                print Human.sex(i,j)
    identity,identity2,action=raw_input("\nEnter a male,female and desired state from sleep|eat|move|sex|end\n").split()
#in the next episode i will have to first add a object reference in the loop for sex method to work. i.e: h.method() in 6 will be male.sex() in 7 
#look at inheretence to see if you can make a seperate gender sub class(might not work) 
"""


"""
#### Try 1
population=True
while population:
    n=raw_input("\nDefine human name and gender with commans and enter 'end,spawn' to end spawing of humans\n").split(",")
    print n[0]
    try:
        if n[1]=="Male" or n[1]=="male":
            m.append(n[0])
        elif n[1]=="Female" or n[1]=="female" :
            f.append(n[0])
        elif n[0]=="end" and  n[1]=="spawn":
            population=False
    except:
        print "gender not defined"
    print m
    print f
male={name:Human(name=name) for name in m}
female={name:Human(name=name) for name in f}
print male
print female
for i in male:
    print i
for j in female:
    print j
"""

"""
for i in n:
    print i
    response=requests.get(url)
    js=response.json()
    n=js["results"][0]["name"].values()
    spawn_name=n[0].lower()
    spawn_gender=js["results"][0]["gender"]
    spawn_name=spawn_name.encode("ascii","ignore")
    s_h={spawn_name:Human(name=spawn_name,gender=spawn_gender)}
    h.update(s_h)
    print("\n")
    print h
    print("\n")
"""



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