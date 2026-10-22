
num = [2,1,4,3,7,5]

def finding_smallest():
    smallest = num[0]
    for i in num:
        if i<smallest:
            smallest = i       
    return smallest
a = finding_smallest()

def finding_largest():
    largest = num[0]
    for i in num:
        if i>largest:
            largest = i    
    return largest
b = finding_largest()
print("Largest number =",b )
print("Smallest number =",a)
            


    
