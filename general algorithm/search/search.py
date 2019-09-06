def binsearch1(arr, l, r, target):
    while l < r:
        mid = (l + r) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1


def binsearch2(arr, l, r, target):
    while l < r:
        mid = (l + r) // 2
        if arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return r + 1 if target == arr[r + 1] else -1


def binsearch3(arr, l, r, target):
    while l < r:
        mid = (l + r) // 2
        if arr[mid] < target:
            l = mid + 1
        else:
            r = mid
    return l


if __name__ == '__main__':
    arr = [1, 2, 3, 4]
    print(binsearch1(arr, 0, len(arr) - 1, 3))
    print(binsearch2(arr, 0, len(arr) - 1, 3))
    print(binsearch3(arr, 0, len(arr) - 1, 3))
