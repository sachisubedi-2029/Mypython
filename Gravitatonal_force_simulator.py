
def gravitational_force(m1,m2,radius):
    G = 6.67*10**-11
    Force = G*(m1*m2)/radius**2
    return Force

m1 = float(input("Enter the mass of first body in kg :"))
m2 = float(input("Enter the mass of the second body in kg :"))
radius = float(input("Enter the distance between the center of both bodies :"))
result1= gravitational_force(m1,m2,radius)
print("The gravitational force betweeen two bodies is",result1,"N")
    
#  What's happens to the gravitational force when m1 is doubled
doubled_m1 = 2*m1
result2 = gravitational_force(doubled_m1,m2,radius)
print("The gravitational force between two bodies is ",result2,"N  when m1 is doubled")

#Comparing result1 and result2
from fractions import Fraction
compare = Fraction(result2/result1).limit_denominator()
print("The new force is 2 times of the original force")

# What's happens to the gravitational force when m1 is halved
halved_m1 = m1/2
result3 = gravitational_force(halved_m1,m2,radius)
print("The gravitational force between two bodies is ",result3,"N when m1 is halved")

compare = Fraction(result3/result1).limit_denominator()
print("The new force is half of the original force.")

# taking m1 and m2 constant 
radius1 = 2*radius
r_result1 = gravitational_force(m1,m2,radius1)
print("The new gravitational force is ",r_result1,"N when distance is doubled")

comparing = Fraction(r_result1/result1).limit_denominator()
print("The new force is one-quarter of the original force.")

# Making distance half
radius2 = radius/2
r_result2 = gravitational_force(m1,m2,radius2)
print("The new gravitational force is",r_result2,"N when distance is halved")

comparing2 = Fraction(r_result2/result1).limit_denominator()
print("The new force is four times the original force.")



