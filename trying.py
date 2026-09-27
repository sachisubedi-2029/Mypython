largest = 0
smallest = 0
a = int(input("enter first number:"))
b = int(input("enter second number :"))
c = int(input("enter third number :"))
d = int(input("enter fourth number :"))
e = int(input("enter fifth number :"))

def find_largest(a,b,c,d,e):
      if a>=b and a>=c and a>=d and a>=e:
         return a
      elif b>=a and b>=c and b>=d and b>=e:
        return b
      elif c>=a and c>=b and c>=d and c>=e:
        return c
      elif d>=a and d>=b and d>=c and d>=e:
        return d
      else:
        return e
largest = find_largest(a,b,c,d,e)

def find_smallest(a,b,c,d,e):
      if a<=b and a<=c and a<=d and a<=e:
         return a
      elif b<=a and b<=c and b<=d and b<=e:
         return b
      elif c<=a and c<=b and c<=d and c<=e:
         return c
      elif d<=a and d<=b and d<=c and d<=e:
         return d
      else:
         return e
smallest = find_smallest(a,b,c,d,e)
print("Greatest number is =",largest)
print("Smallest number is =",smallest)
