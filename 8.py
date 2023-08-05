#find the sum of ingers in list
List=[]
Limit=int(input('enter the list limit\n'))

def add_values(value,li):
    li.append(value)

def list_sum(li):
    sum=0
    for i in li:
        sum+=i
    return print(f'sum of the  list {sum}')    

for i in range(0,Limit):
    x=int(input(f'enter values to the list {List} \n')) 
    add_values(x,List)


list_sum(List)

