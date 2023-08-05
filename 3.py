# 
List=[]
Limit=int(input('enter the limit \n'))

def add_values(value,li):
    li.append(value)

def as_sort(li):
    limit=Limit
    for i in range(0,limit):
        for j in range(i+1,limit):
            if(li[i]>li[j]):
                temp=li[i]
                li[i]=li[j]
                li[j]=temp

    global List
    List=li   
             

for i in range(0,Limit):
    x=int(input(f'enter values to the array {List}'))
    add_values(x,List)

print(F"before the Ascending  {List} \n")

as_sort(List)

print(F"after the Ascending sort List{List}")
