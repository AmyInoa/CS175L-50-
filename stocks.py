#AmyInoa
#CS 175 Lab
#Stocks

commission_rate = float(input("what is the commission rate?: "))
shares_purchased = int(input("how many shares did you purchase?: "))
amount_paid_for_stock = float(input("what was the purchase price?: "))
price_per_share = float(input("what was the selling price?: "))

amount_paid_for_stock = shares_purchased * amount_paid_for_stock
print('\nAmount of money paid for the stock = $',
      format(amount_paid_for_stock, ',.2f'),
      sep='')

commission_paid_when_bought = amount_paid_for_stock * commission_rate
print('Amount of commission paid to broker when Joe bought the stock = $',
      format(commission_paid_when_bought, ',.2f'),
      sep='')

amount_stock_sold_for = shares_purchased * price_per_share
print('Amount for which Joe sold the stock = $',
      format(amount_stock_sold_for, ',.2f'),
      sep='')

commission_paid_when_sold = amount_stock_sold_for * commission_rate
print('Amount of commission paid to broker when Joe sold the stock = $',
      format(commission_paid_when_sold, ',.2f'),
      sep='')

totalcommissionpaid = commission_paid_when_bought + commission_paid_when_sold
print('\nATotal commission paid = $',
      format(totalcommissionpaid, ',.2f'),
      sep='')

totalprofit = (amount_stock_sold_for - amount_paid_for_stock) - totalcommissionpaid
print('\nTotal profit = $',
      format(totalprofit, ',.2f'),
      sep='')



