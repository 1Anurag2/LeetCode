from typing import List

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        key_indices = [i for i, num in enumerate(nums) if num == key]
        result_set = set()

        for j in key_indices:
            for i in range(max(0, j - k), min(n, j + k + 1)):
                result_set.add(i)

        return sorted(result_set)
