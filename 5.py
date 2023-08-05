def is_prime(number):
    c=0
    if number==1:
        return print('oops 1 is not a prime')
    else:
       for i in range(1,number+1):
          if(number%i==0):
              c+=1

       if(c==2):
          return print(f'{number} is a prime') 
       else:
          return print(f'{number} is not a prime')
            
      
num=int(input('enter a number to check prime or not \n'))
is_prime(num)

