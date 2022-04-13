#Amy Inoa
#CS 175L
#expensePieChart

import matplotlib.pyplot as plt
import numpy as np

file = open('expenses.txt', 'r')

expenses = ['Rent', 'Gas', 'Food',
		'Clothing', 'Car payment', 'Misc']

data = [1000, 250, 350, 200, 375, 800]

fig = plt.figure(figsize =(10, 7))
plt.pie(data, labels = expenses)


plt.show()




