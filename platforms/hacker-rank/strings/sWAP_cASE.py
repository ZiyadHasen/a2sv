def swap_case(s):
    
    result=[]
    for i in range(len(s)):
        if s[i].isupper():
            result.append(s[i].lower())
        else:
             result.append(s[i].upper())  
         
    return ''.join(result)
