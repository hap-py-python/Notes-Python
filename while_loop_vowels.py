
vowels = ['a', 'e', 'i', 'o', 'u']

length = len(vowels)
print(length)

i = 0 # creating loop variable i

while i < len(vowels):  # condition for the loop
    print(vowels[i] + '', end = '')  # printing vowel of i + '', end = '' means that it is going to be on the same line
    i += 1  # means that every new loop goes forward to another element (vowel)
