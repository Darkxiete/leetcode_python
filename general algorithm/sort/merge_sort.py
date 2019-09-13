class MergeSort1:
    """
    Recursive version
    """
    def merge(self, left, right) -> list:
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

    def mergesort(self, arr) -> list:
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = self.mergesort(arr[:mid])
        right = self.mergesort(arr[mid:])
        ans = self.merge(left, right)
        return ans


class MergeSort2:
    """
    Iterative version
    """
    def merge(self, arr, tmp, lo, mid, hi):
        k = i = lo
        j = mid + 1
        while i <= mid and j <= hi:
            if arr[i] < arr[j]:
                tmp[k] = arr[i]
                k += 1
                i += 1
            else:
                tmp[k] = arr[j]
                k += 1
                j += 1
        while i < len(arr) and i <= mid:
            tmp[k] = arr[i]
            i += 1
        for i in range(lo, hi):
            arr[i] = tmp[i]

    def mergesort(self, arr, tmp, low, high):
        size = 1
        while size <= high - low:
            for i in range(low, high, 2 * size):
                lo = i
                mid = lo + size - 1
                hi = min(i + 2 * size - 1, high)
                self.merge(arr, tmp, lo, mid, hi)
            size *= 2


if __name__ == '__main__':
    m = MergeSort2()
    nums = [4, 2, 1, 6, 2, 3, 6, 7, 1, 11]
    mid = len(nums) // 2
    m.mergesort(nums, [0] * len(nums), 0, len(nums) - 1)
    print(nums)
