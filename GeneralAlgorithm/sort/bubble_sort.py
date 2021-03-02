def _bubblesort(arr, l, r):
    while l < r:
        if arr[l] > arr[l + 1]:
            arr[l], arr[l + 1] = arr[l + 1], arr[l]
        l += 1


def bubblesort(arr):
    for i in range(len(arr)):
        _bubblesort(arr, 0, len(arr) - 1)


if __name__ == '__main__':
    arr = [3, 2, 4, 1, 5]
    bubblesort(arr)
    print(arr)
