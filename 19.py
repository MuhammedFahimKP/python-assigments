"find the sum of digits in a given number"
num=int(input('enter the number to find sum of digit \n'))
def sum_of_digits(Number):
    number=str(Number)
    sum=0
    for i in number:
        sum+=int(i)
        

    print(f'sum of digits {sum}') 

sum_of_digits(num)