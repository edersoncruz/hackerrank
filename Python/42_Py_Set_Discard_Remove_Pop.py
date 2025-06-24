# Question Link
# https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem?isFullScreen=true

number_elements = input()
entry = input()
set_ = set(map(int, entry.split()))
number_operations = int(input())

for i in range(number_operations):
    entry_ = input().split()

    if len(entry_) == 2:
        operation, value_str = entry_
        value = int(value_str)
    else:
        operation = entry_[0]

    if operation == 'remove':
        try:
            set_.remove(value)
        except KeyError:
            pass

    elif operation == 'discard':
        set_.discard(value)

    elif operation == 'pop':
        if set_:
            set_.remove(min(set_))

sum_set = sum(set_)
print(sum_set)
