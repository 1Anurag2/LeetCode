from typing import List
from itertools import permutations
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        all_combinations = []
        for i in permutations(nums):
            all_combinations.append(i)
            string_tupples = [''.join(str(x) for x in tup) for tup in all_combinations]
        max_string = max(string_tupples)
        return max_string
    
sol = Solution()
print(sol.largestNumber([1,2,3,4,5,6,7,8,9,0]))