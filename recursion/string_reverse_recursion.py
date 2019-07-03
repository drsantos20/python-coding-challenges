
def reverse(word):
    if len(word) == 0:
        print(word)
        return word
    else:
        print(word)
        return reverse(word[1:]) + word[0]


word = 'Geeksforgeeks'


print('The original string  is : ', end='')
print(word)

print('The reversed string(using recursion) is : ', end='')
print(reverse(word))
