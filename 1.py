a=[]
n=int(input('enter the length of the list \n'))
def add_values(value,index,li):
    li.insert(index,value)

def max_elemnt(b):
    max_el=b[0]
    for i in range(1,len(b)):
        if b[i]>max_el :
            max_el=b[i]

    return print(f"is the largest elemnt of the list {max_el}")    

for i in range(0,n):
    x=int(input(f"enter the values to the list {a}\n"))
    add_values(x,i,a)  
    if(i==n-1):
        choice=str(input("if want to print max elment Y-yes N-no\n"))
        if choice=='Y' or choice=='y':
            max_elemnt(a)
        elif choice=='N' or choice=='n':
            print(' ')
        else:
            print("in valid entry")    

    

        





        



