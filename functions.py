def myfunc(*s):
    output=""
    for i in range(len(s)):
        if (i+1)%2==1:
            output=output+s[i].upper()
        else:
            output=output+s[i].lower()    
    return output 
k=myfunc('abcdefg')
print(k)