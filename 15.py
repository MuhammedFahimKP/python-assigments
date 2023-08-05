""" 
   sum of prime number with in the given limit  
"""
n=int(input('enter the limit\n '))
def sum_of_prime(limit):
    sum=0
    for i in range(1,limit+1):
        c=0
        for j in range(1,i+1):
            if i%j==0 :
                c+=1
        if c==2 :
            sum+=i
    return print(f'sum of the prime nummber {sum}')     


sum_of_prime(n)
