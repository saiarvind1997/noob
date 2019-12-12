import random
a=ord('a')
z=ord('z')+1
color=['Violet','Indigo','Blue','Green','Yellow','Orange','Red']

while a<z:
    i=1
    while i<10:
        ran_color=random.choice(color)
        print'{}{},{}'.format(chr(a),i,ran_color)
        i+=1
    a+=1