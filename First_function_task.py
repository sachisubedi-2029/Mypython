def calculate_bill(units):
    if units<0:
        print("Invalid")
    elif units>=0 and units<=100:
        price = units*5
        print("Your total bill is Rs.",price)
    elif units>100 and units<=200:
        extra = units-100
        price = 100*5 + extra*7
        print("Your bill is Rs.",price)
    else:
        extra = units-200
        price = 100*5 + 100*7 + extra*10
        print("Your bill is Rs.",price)
consumption = int(input("Enter electricity consumption in units :"))
calculate_bill(consumption)




