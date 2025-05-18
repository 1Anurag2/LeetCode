class Solution:
    def smallestIndex(self, nums):
        def digit_sum(n):
            return sum(int(d) for d in str(abs(n)))  # Use abs to support negative numbers if any

        for i, num in enumerate(nums):
            if digit_sum(num) == i:
                return i
        return -1
