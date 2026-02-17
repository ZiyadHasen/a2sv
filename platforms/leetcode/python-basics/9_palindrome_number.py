# The general idea is just make the intiger itarable(string) so that you will have controll to indidvidual elements 

def isPalindrome( x: int) -> bool:
    string = str(x)
    if string == string[::-1]:
        return True
    else:
        return False
    
    # or simply 
    # x= str(x) 
    # return x == x[::-1]



print(isPalindrome(121))

