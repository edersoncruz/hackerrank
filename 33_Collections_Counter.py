# Question Link https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=true

from collections import Counter

number_of_shoes = input("Number: ")
sizes_of_shoes_entrada = input('Size: ')
sizes_of_shoes_list = sizes_of_shoes_entrada.split()
sizes_of_shoes_counter = Counter(sizes_of_shoes_list)
number_of_customers = int(input('Number of Customers: '))
total = 0

for _ in range(number_of_customers):
    key, value = input('Purchase: ').split()
    value_int = int(value)

    if key in sizes_of_shoes_counter:
        total += value_int
        sizes_of_shoes_counter[key] -= 1

        if sizes_of_shoes_counter[key] == 0:
            del sizes_of_shoes_counter[key]

print(total)