# -*- coding: utf-8 -*-
"""Fruit Dictionary Exercise

Create a dictionary called fruit_prices that contains the prices of fruits. The prices are as follows:

apple: 1500
banana: 1000
orange: 1200

Then write code that changes the price of banana to 1100 and removes apple altogether. Finally, print this dictionary.
"""

# create first dictionary
fruit_prices = {
    'apple': 1500,
    'banana': 1000,
    'orange': 1200
}

# change banana price
fruit_prices['banana'] = 1100

# delete apple
del fruit_prices['apple']

# print dictionary
print(fruit_prices)

