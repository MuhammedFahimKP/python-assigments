#print prime numbers from 1 to given limit 
Limit = int(input('enter the limit to prime number\n'))
def prime_number(limit):
   
    for i in range(1,limit+1):
        c=0
        for j in range(1,i+1):
            if i%j==0:
                c+=1
        if c==2:
            print(f'\n{i}\n')

prime_number(Limit)
         