import requests
class Human:
    def __init__(self,name):
        self.name=name
        #self.gender=gender
        #self.male="Male"
        #self.female="Female"
class sex:
    def sex(cls,gender1,gender2):#cls(similar to self) refers to the init by constructing the above class.
        if gender1==cls.male and gender2==cls.female:
            return "sex is possible"
        else:
            return "sex is not possible"
url="https://randomuser.me/api/"
i=0
n=raw_input("\nDefine human names with commas\n").split(",")
h={name:Human(name=name) for name in n}
print h
for i in range(0,10):
    response=requests.get(url)
    js=response.json()
    n=js["results"][0]["name"].values() #to find and search for the values. 1st results and then name. think of it as nested
    spawn_name=n[0].lower()
    spawn_name=spawn_name.encode("ascii","ignore")
    s_h={spawn_name:Human(name=spawn_name)}
    h.update(s_h)
    print("\n")
    print h.keys()
    print("\n")
    spawn_gender=js["results"][0]["gender"]
    print spawn_gender
    i+=1
"""
    TASK 7

This time I will type 

mm gg sex

calories should be full for both or else it should say not enough calories for that action

It should create a baby and this time it should get the name from 

https://randomuser.me/api/

use only the first name and make it all lowercase before making the baby
"""


