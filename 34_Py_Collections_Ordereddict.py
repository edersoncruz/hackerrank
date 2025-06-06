# Question Link https://www.hackerrank.com/challenges/py-collections-ordereddict/problem?isFullScreen=true

from collections import OrderedDict

item_sales = OrderedDict()
number_purchases = int(input())

for _ in range(number_purchases):
    item, quantity = input().rsplit(" ", 1)
    
    if item in item_sales:
        item_sales[item] += int(quantity)
    else:
        item_sales[item] = int(quantity)
    


for item in item_sales:
    print(item, item_sales[item])