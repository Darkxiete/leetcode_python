from typing import List


class Solution:
    def maxArea1(self, height: List[int]) -> int:
        m = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                area = (j - i) * min(height[j], height[i])
                if m < area:
                    m = area
        return m

    def maxArea2(self, height: List[int]) -> int:
        if len(height) == 2:
            return min(height[0], height[1])
        i = 0
        j = len(height) - 1
        hl = height[i]
        hr = height[j]
        m = (len(height) - 1) * min(height[i], height[j])
        while i < j:
            while i < j and height[i + 1] < hl:
                i += 1
            i += 1
            if i > j:
                break
            hl = height[i]
            tmp = (j - i) * min(height[i], height[j])
            if m < tmp:
                m = tmp
            while i < j and height[j - 1] < hr:
                j -= 1
            j -= 1
            if i > j:
                break
            hr = height[j]
            tmp = (j - i) * min(height[i], height[j])
            if m < tmp:
                m = tmp
        return m


if __name__ == '__main__':
    height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    height2 = [10,9,8,7,6,5,4,3,2,1]
    s = Solution()
    assert s.maxArea1(height1) == 49
    assert s.maxArea2(height1) == 49
    assert s.maxArea2(height2) == 25
