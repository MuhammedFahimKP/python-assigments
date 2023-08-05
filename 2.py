# string_reverse
string=str(input(f"enter   to the list\n"))

def reverse_str(my_string):
    if type(my_string)!=str():
        return print(f"Oops ! is not {my_string} a string object")
    else:
        n=len(my_string)
        i=0
        j=n-1
        v=str()
        for i in range(n-1,-1,-1):
            v+=my_string[i]    

        global string
        string=v             
        return string    



print(f"string before rverese {string} \n")
reverse_str(string)
print(f"sting after reverse {string} \n")