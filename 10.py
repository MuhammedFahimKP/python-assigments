# max and min element of a list
List=[]
Limit = int(input('enter the limit of the list\n'))

def add_values(value,li):
    li.append(value)
def max_min_in_list(li):
    max=li[0]
    min=li[0]
    for i in range(1,len(li)):
        if li[i]>max:
            max=li[i]
        elif li[i]<min:
            min=li[i] 

    return print(f'max elment of the list {max} \n min elment of the list {min}') 

for i in range(0,Limit):
    x=int(input(f'enter values to the list {List} \n')) 
    add_values(x,List)

max_min_in_list(List)  