from typing import List
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(len(arr)-2):
            if(arr[i] % 2 != 0 and arr[i+1] % 2 != 0 and arr[i+2] % 2 != 0):
                return True
        return False
                
sol = Solution()
arr = [2,6,4,1]
arr1 = [1,2,34,3,4,5,7,23,12]
print(sol.threeConsecutiveOdds(arr))
print(sol.threeConsecutiveOdds(arr1))