#Using the difference attribute to create an even number set from whole numbers and odd number. 

#Set

whole_numbers = set(range(0, 20, 1))
odd = set(range(1, 20, 2))
even = whole_numbers.difference(odd)

#Execution

print(even)
print(odd)
print(whole_numbers)