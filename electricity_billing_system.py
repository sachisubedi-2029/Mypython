valid = 0
highest_bill = 0
total_money = 0
greater_bill = 0

while True:
    consumption = int(input("Enter your electricity consumption in units :"))
    if consumption==-1:
        break
    else:
        if consumption<0:
            print("Invalid consumption")
        elif consumption>=0 and consumption<=20:
            cost=consumption*5
            print("Your total bill is Rs.",cost)
            valid = valid+1
            total_money =total_money+cost
            if cost>highest_bill:
                highest_bill=cost
        elif consumption>20 and consumption<=50:
            extra = consumption-20
            cost =(20*5)+(extra*8) 
            print("Your total bill is Rs.",cost)
            valid = valid+1
            total_money=total_money+cost
            if cost>highest_bill:
                highest_bill=cost
        elif consumption>50 and consumption<=100:
            extra=consumption-50
            cost=(20*5)+(30*8)+(extra*12)
            print("Your total bill is Rs.",cost)
            valid=valid+1
            total_money=total_money+cost
            if cost>highest_bill:
                highest_bill=cost        
        elif consumption>100 and consumption<=200:
            extra=consumption-100
            cost=(20*5)+(30*8)+(50*12)+(extra*18)
            print("Your total bill is Rs.",cost)
            total_money=total_money+cost
            valid=valid+1
            if cost>highest_bill:
                highest_bill=cost
            if cost>=2000:
                print("High consumption bill")
                greater_bill=greater_bill+1
        else:
              print("Heavy consumption")
              extra=consumption-200
              cost=(20*5)+(30*8)+(50*12)+(100*18)+(extra*25)
              print("Your total bill is Rs.",cost)
              if cost>=2000:
                print("Heavy consumption bill")
                greater_bill=greater_bill+1
              valid=valid+1   
              total_money=total_money+cost
              if cost>highest_bill:
                highest_bill=cost
print("Number of valid households =",valid)
print("total money collected = Rs.",total_money)
if total_money>0:
    average_bill=total_money/valid
    print("Highest bill = Rs.",highest_bill)
    print("Average bill per household = Rs.",average_bill)
else:
    print("No money collected")
print("Number of households with bills more than or eqaul to Rs.2000 =",greater_bill)                        

