#amstron number
def isAmstrong(Number):
    if type(Number)!=int:
        return print(f"Opps {Number} is  not an intger object")
    else:
        result=0
        num=Number
        n=len(str(Number))
        while(Number!=0):
            digit=Number%10
            result=result+digit**n

            Number=Number//10       
        if num==result:
            print(f"{num}  is an  amstrong  ")
        else:
            print(f"{num}  not an  amstrong  ")    

isAmstrong(2000)

        

