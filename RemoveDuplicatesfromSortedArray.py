from typing import List
from collections import Counter 
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # single_list_value = Counter(nums)
        # result_list = []
        # for value , freq in single_list_value.items():
        #     result_list.append(value)
        # return len(result_list)

        if not nums:
            return 0
        
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        
        return i + 1

sol = Solution()
nums1 = [0,0,1,1,1,2,2,3,3,4]
print(sol.removeDuplicates(nums1))

nums2 = [1,1,2]
print(sol.removeDuplicates(nums2))
