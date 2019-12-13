c=ord('a')
d=ord('z')+1
while c<d:
    i=1
    while i<10:
        print'{}{}'.format(chr(c),i)
        i+=1
    c+=1

#alternate code with for loops:
"""
x= ord("a")
y= ord("z")+1
for c in range(x,y):
    for i in range(1,10):
        print "{}{}".format(chr(c),i)
"""