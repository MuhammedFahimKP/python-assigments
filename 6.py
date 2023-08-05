List=[]
Limit=int(input('enter the list limit\n'))

def add_values(value,li):
    li.append(value)

def sec_large(li):
    if li[0]<li[1]:
        sec=li[0]
        lar=li[1]

    else :
        sec=li[1]
        lar=li[0]

    for i in range(2,Limit):
        
        if li[i]>lar and li[i]<sec:
            sec=lar
            lar=li[i]
        elif li[i]<lar and li[i]>sec:
            sec=li[i]

    return print(f"Second largest in the list {sec} and largest {lar}")            





for i in range(0,Limit):
    x=int(input(f'enter values to the list {List}'))
    add_values(x,List)

sec_large(List)
