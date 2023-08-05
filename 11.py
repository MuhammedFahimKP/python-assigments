#factorial of  given number
def factorial():
    n=1
    limit = int(input('enter the num '))
    for i in range(1,limit+1):
        n = n*i
    return print(f'factorial of {n}')

factorial()