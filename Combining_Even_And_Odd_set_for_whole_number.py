#Combining odd and even numbers to get whole number set. 

#sets

even = set(range(0, 20, 2))
odd = set(range(1, 20, 2))

whole_number = even.union(odd)

#Execution

print(odd)
print(even)
print(whole_number)