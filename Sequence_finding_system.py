
def finding_sequence(a,b,c):
    num_zero = 0
    if a==0:
      num_zero=num_zero+1
    if b==0:
      num_zero=num_zero+1
    if c==0:
      num_zero=num_zero+1

    if num_zero==3:
      return "All numbers are zero" 
    elif num_zero==2:
      return "Two numbers are zero" 
    elif num_zero==1:
      return "One number is zero"
    else:
      diff1  = b-a
      diff2  = c-b
      ratio1 = b/a 
      ratio2 = c/b
      if diff1==diff2:
        return "Arithmetic Sequence"
      elif ratio1==ratio2:
        return "Geometric sequence"
      else:
        return "Neither"    
a = int(input("Enter first number :")) 
b = int(input("Enter second number :"))
c = int(input("Enter third number :"))
result = finding_sequence(a,b,c)   
print(result)    
