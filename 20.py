"total count vowels in a string"
string=str(input('enter a string\n'))
def vowels(String):
    c=0
    for i in String:
        if i=='a' or i=='e' or i=='i'or i=='u' or i=='o' or i=='A' or i=='E' or i=='I' or i=='U'or i=='O':
            c+=1

    print(f'{c} vowels in the string  object {String}') 
    