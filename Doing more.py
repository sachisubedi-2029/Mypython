
num = [3,4,1,1,3,56]

def finding_even_odd():
    even = 0
    odd = 0
    for i in num:
        if i%2==0:
            even = even+1
        else:
            odd = odd+1
    return even,odd
a,b = finding_even_odd()
print("The number of even =",a)
print("The number of odd =",b)        
            





