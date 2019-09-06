def merge(left, right) -> list:
    size1 = len(left)
    size2 = len(right)
    result = []

    i, j, k = 0, 0, 0
    while i < size1 and j < size2:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        k += 1

    if i < size1:
        result += left[i:]
    if j < size2:
        result += right[j:]
    return result


def mergesort(arr) -> list:
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    ans = merge(left, right)
    return ans


if __name__ == '__main__':
    nums = [4, 2, 1, 6, 2, 3, 6, 7, 1, 11]
    mid = len(nums) // 2
    print(mergesort(nums))
