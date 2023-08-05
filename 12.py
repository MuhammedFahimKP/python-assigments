# given string palindrome or not 
my_string=str(input('enter the string \n'))
def is_pallindrom(string):
    if type(string)!=str:
        return print(f'Opps {string} is not  a string object')
    else :
        i=0
        j=len(string)-1
        c=0
        p=(len(string)//2)-1
        while(i<p):
            if string[i]==string[j]:
                c+=1
                
            j-=1
            i+=1
        if c == p:
            print('\nis palindrom')
        else:
            print('\nis not palindrom ')

        return string


is_pallindrom(my_string)          
