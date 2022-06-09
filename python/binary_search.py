def binary_search(num, arr):
    l, r = 0, len(arr)

    while l < r:
        index = (r + l)//2
        if num == arr[index]:
            return index
        elif num > arr[index]:
            l = index + 1
        elif num < arr[index]:
            r = index - 1

    return -1



print(binary_search(130, range(100, 200, 3))) # should be 10