"union of 2 list"

Li1=[]
Li2=[]

limit1=int(input('enter the limit of first list\n'))

for  i in range(limit1):
    x=int(input(f'enter the values to the list {Li1} \n'))
    Li1.append(x)

limit2=int(input('enter the limit of second list\n'))

for  i in range(limit2):
    x=int(input(f'enter the values to the list {Li2} \n'))
    Li2.append(x)

def union(li1,li2):
    li3=li1+li2
    return li3


 
print(f'after union {union(Li1,Li2)}\n')
