List=[]
Limit=int(input('enter the list limit\n'))

def add_values(value,li):
    li.append(value)

def remove_duplicte(li):
    result=[]
    global List
    for i in li:
        if i not in result:
            result.append(i)
    
    List=result
    return List




for i in range(0,Limit):
    x=int(input(f'enter values to the list {List} \n')) 
    add_values(x,List)

print(f"before removing duplicate {List} \n")

remove_duplicte(List)

print(f"before removing duplicate {List} \n")
