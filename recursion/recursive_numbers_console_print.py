

def print_numbers(number):
    print(number)

    if number < 0:
        # base case for recursion, this means that reaching this condition the function will stop here
        return
    else:
        # recursive case for recursion, this means that we will call the function again
        print_numbers(number-1)


print_numbers(5)
