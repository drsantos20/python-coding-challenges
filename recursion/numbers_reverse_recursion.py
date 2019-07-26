

def reverse_numbers(test):

    if test < 1:
        return
    else:

        print(test, end=" ")
        reverse_numbers(test - 1)
        print(test, end=" ")
        return


test = 3
reverse_numbers(test)
