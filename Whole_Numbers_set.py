#Getting whole number set from even and odd numbers.

odd = set(range(1, 10, 2))
even = set(range(0, 10, 2))

whole_numbers = odd.union(even)

print(whole_numbers)