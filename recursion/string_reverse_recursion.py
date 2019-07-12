
def reverse(word):
    if len(word) == 0:
        return word
    else:
        return reverse(word[1:]) + word[0]


word = 'Daniel'


print('The original string  is : ', end='')
print(word)

print('The reversed string(using recursion) is : ', end='')
print(reverse(word))
