import sys

type=sys.argv[1]
a = sys.argv[2]
b = sys.argv[3]

if "sum"==type:
    c= int(a) + int(b)
    print "sum is %s" %c
elif "diff"==type:
    c= int(a) - int(b)
    print "diff is %s" %c
elif "mul"==type:
    c= int(a) * int(b)
    print "mul is %s" %c
elif "div"==type:
    c= int(a) / int(b)
    print "div is %s" %c
print "Sum|Diff|Mul|Div"       