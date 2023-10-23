def hoarsePartition(arr, l, h):
    pivot = arr[l]

    i = l - 1
    j = h + 1

    while True:

        i = i + 1
        while arr[i] < pivot:
            i = i + 1

        j = j - 1
        while arr[j] > pivot:
            j = j - 1

        if i >= j:
            return j

        arr[i], arr[j] = arr[j], arr[i]


# arr=[8, 4, 7, 9, 3, 10, 5]

# hoarsePartition(arr, 0, 5)

# print(*arr)

