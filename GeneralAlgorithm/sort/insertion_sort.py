def insertion_sort(arr):
    for i in range(1, len(arr)):
        index = _search(arr, 0, i, arr[i])
        _insert(arr, index, i)


def _search(arr, start, end, e):
    """
    从arr[start: end]，找一个不大于`e`的数，放在其右边
    :param arr:
    :param start:
    :param end:
    :param e:
    :return:
    """
    while start < end:
        if e >= arr[end - 1]:
            return end
        end -= 1
    return 0


def _insert(array, i, j):
    """
    将arr[j]插入到`i`索引中
    :param arr:
    :param i:
    :param j:
    :return:
    """
    tmp = array[j]
    while i < j:
        array[j] = array[j - 1]
        j -= 1
    array[i] = tmp


if __name__ == '__main__':
    arrs = (
        [3, 2, 2, 3, 1, 4],
        [1],
        [3, 2, 1]
    )
    for arr in arrs:
        print(arr)
        insertion_sort(arr)
        print(arr)
