#Creating a program that will copy an odd number list and convert it into an even number list.

#Creating the list. 

odd = list(range(1, 60, 2))
even = odd.copy()

for repeat in range(0, 30):
    even.pop()
even.extend(list(range(2, 60, 2)))
print(odd)
print(even)