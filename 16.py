"sum of products of 5 and 3 from the given limit"

Limit=int(input('enter the Limit'))
def sum_product_of_3_or_5_from_1(Limit):
    sum=0
    for i in range(1,Limit):
        if i%3==0 or i%5==0:
            sum+=i

    return print(f'{sum} is sum ')        

sum_product_of_3_or_5_from_1(Limit)