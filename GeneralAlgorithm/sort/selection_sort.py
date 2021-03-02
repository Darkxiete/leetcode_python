def selection_sort(arr):
    """
    从左到右，每次选区间里最大的放在
    :param arr:
    :return:
    """
    for i in range(len(arr)):
        m = arr[0]
        index = 0
        for j in range(len(arr) - i):
            if arr[j] >= m:
                m = arr[j]
                index = j
        arr[index], arr[len(arr) - i - 1] = arr[len(arr) - i - 1], arr[index]


if __name__ == '__main__':
    nums = [3, 2, 1, 3, 4, 5]
    selection_sort(nums)
    print(nums)

