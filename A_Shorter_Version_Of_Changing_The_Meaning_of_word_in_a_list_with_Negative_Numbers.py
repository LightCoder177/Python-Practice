#A shorter version of changing the meaning of a word in a list.


#list and variable.

phrase = "Don't panic!"
plist = list(phrase)

#changes and execution

new_phrase = (''.join(plist[-10:-12:-1]) + ''.join([plist[-7], plist[-6],plist[-5], plist[-3], plist[-4]]) + ".")

print(phrase)
print(new_phrase)