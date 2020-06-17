#not a task
#high and low
import random
holder=True
num=random.randrange(1,100)
attempts=12
while holder!=False:
    print ("\nThe number of remaining attempts are: %s\n" % (attempts))
    try:
        usernum=int(raw_input("Guess the number:\n"))
        attempts-=1
        while num!=usernum and attempts!=0:
            if usernum<num:
                print"Lower\nattempts rempaining=%s\n" % attempts
            else:
                print "Higher\nattempts rempaining=%s\n" % attempts
            
            usernum=int(raw_input("Guess the number:\n"))
            attempts-=1
        else:
            if num==usernum:
                print "You Win!!!\nremaining attempts are %s" % attempts
            else:
                print "you Lose!!!\nremaining attempts are 0"
            holder=False 
    except ValueError:
        print "This is an not a number" 
   
    
    
