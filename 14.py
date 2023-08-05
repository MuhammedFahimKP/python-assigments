#fibnonacci number from 1 to given limit
n=int(input('enter the limit '))
def fibnonacci(n):
    num1 = 0
    num2 = 1
    next_number = num2
    for i in range(1,n+1):
        print(f"{next_number}\t" ,end="")
        num1, num2 = num2, next_number
        next_number = num1 + num2

fibnonacci(n)        