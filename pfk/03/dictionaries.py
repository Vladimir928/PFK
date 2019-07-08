#!/usr/bin/env python3
################################################################################
#   dictionaries.py
#
#   chapter 3: Dictionaries
#
#   08.07.2019  Created by:  vo958
################################################################################

currencies = {'Russia': 'Rub', 'USA': 'USD', 'France': 'EURO'}
print(currencies)
print(currencies['USA'])
print(type(currencies))

print('\nKeys and Values')
keys = currencies.keys()
print(type(keys))
print(keys)
values = currencies.values()
print(type(values))
print(values)

for key in keys:
    print(key + ': ' + currencies[key])