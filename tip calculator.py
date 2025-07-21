print("Welcome to the tip calculator.!")
amount =float(input("enter the amount of the bill"))
tip=int(input("how much would you like to tip the restaurant 10 ,12,15"))
total_bill=tip/100*amount +amount
final=round(total_bill,2)
print(f" the total amount of the bill is {final}")
