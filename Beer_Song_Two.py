# Beer counting song.

# variable.

word = "bottles"

# loop, condition, and execution

for num_bottle in range(99, 0, -1):
    print(num_bottle, word, "of beer on the wall.")
    print(num_bottle, word, "of beer.")
    print("Take one down.")
    print("Pass it around.")

    if num_bottle == 1:
        print("No more bottles of beer on the wall.")
    else:
        new_num = num_bottle - 1
        if new_num == 1:
            word = "bottle"
        print(new_num, word, "to go.")
    print()
