

def insertion_sort(arr):
    for i in range(len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        idx = i - 1
        while idx >= 0 and key < arr[idx]:
            arr[idx + 1] = arr[idx]
            idx -= 1
        arr[idx + 1] = key


insertion_sort([4, 3, 2, 10, 12, 1, 5, 6])
