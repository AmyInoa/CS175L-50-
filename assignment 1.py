#Amy Inoa
#CS 175
#Assignment: 1

#sales prediction
ANNUAL_PERCENT = 0.23
totalSales = float(input("How much was made in total sales this year?: $"))
profit = totalSales * ANNUAL_PERCENT
print(f"For ${totalSales:,.2f} in sales, "
      f"the company made ${profit:,.2f} in profit this year.")

print("")
#total Purchase
TAX_RATE = 0.07
x=0
itemList = 0
while(x < 5):
    item = input(f"Enter the name of item {x+1}: ")
    itemList = itemList + item +  ", "
    price = subtotal + price
    x=x+1
salesTax = subtotal * TAX_RATE
total = subtotal + salesTax
print(f"For a shopping list of {itemList} \nThe subtotal is ${subtotal:,.2f},"
      f"\nThe sales tax is ${salesTaxz:,.2f}, \nAnd the total is ${total:.2f}.")

print("")
#Miles-per-gallon
miles = float(input("How many miles have you driven in your car?: "))
gallons = float(input("How many gallons of gas did it use for those miles?: "))
MPG = miles / gallons
print(f"your car's miles-per-gallon is {MPG:,.2f}.")
