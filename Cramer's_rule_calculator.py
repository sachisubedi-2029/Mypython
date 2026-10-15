# Using cramers rule for two linear equations
# a1x + b1y = c1 and a2x + b2y = c2

def finding_x_y(a1,a2,b1,b2,c1,c2):
  D = a1*b2 - a2*b1
  print("D ",a1,"*",b2,"-",a2,"*",b1,"=", D)
  Dx = c1*b2 - c2*b1
  print("Dx =",c1,"*",b2,"-",a2,"*",b1,"=", Dx)
  Dy = a1*c2 - a2*c1
  print("Dy =",a1,"*",c2, "-",a2,"*",c1,"=", Dy)

  if D!=0:
    x = Dx/D
    print("The determinant is not zero. So,")
    print("x = Dx/D =",Dx/D,"=",x)
    y = Dy/D
    print("y = Dy/D =",Dy/D,"=",y)
    return x,y 
  else:
    print("No unique solutions of x and y if D=0")  

# Taking input from user
a1 = float(input("Enter a1 of your linear equations :"))
a2 = float(input("Enter a2 of your linear equations :"))
b1 = float(input("Enter b1 of your linear equations :"))
b2 = float(input("Enter b2 of your linear equations :"))
c1 = float(input("Enter c1 of your linear equations :"))
c2 = float(input("Enter c2 of your linear equations :"))

result = finding_x_y(a1,a2,b1,b2,c1,c2)
if result is not None:
   a,b = result
   print("The values of  x",a)
   print("The values of y", b)
