#Creating a program that will take even number from the odd number list and put it right back in their rightful place. 

#Variables and list

Odd = [1, 3, 5, 7, 6, 9, 10, 11, 12, 13, 14, 15, 17, 19, 21, 23, 25]

Even = list(range(2,30, 2))

for number in Odd: 
    if number in Even:
        Odd.remove(number)
print(Odd)
print(Even)
