"sum of even and odd numbers sepreatly  from  given limit"
n=int(input('enter the limit\n'))
def sum_of_even_and_odd(limit):
    sum_of_odd=0
    sum_of_even=0
    for i in range(1,limit+1):
        if i%2==0:
            sum_of_even+=i
        else:
            sum_of_odd+=i 

    return print(f'sum of  odd numbers  {sum_of_odd} \nsum of even numbers {sum_of_even}')
        

sum_of_even_and_odd(6)