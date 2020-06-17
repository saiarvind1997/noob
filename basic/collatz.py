def collatz(n):
    if n%2==0:#even
        n=n/2
        return n
    elif n%2==1:#odd
        n=3*n+1
        return n
cur_num=int(raw_input("Enter starting number\n"))
while cur_num!=1:
    seq=collatz(cur_num)
    print seq
    cur_num=seq

"""Write a function named collatz() that has one parameter named number. 
If number is even, then collatz() should print number // 2 and return this value. 
If number is odd, then collatz() should print and return 3 * number + 1"""