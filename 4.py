def sum_of_even_no():
    sum=0
    limit = int(input('enter the limit of the even number to find sum \n'))
    for i in range(1,limit+1):
        if i%2==0:
            sum+=i

    return print(F"sum of {limit} even is {sum}")

sum_of_even_no()        

