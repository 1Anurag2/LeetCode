class Solution:
    def threeSum(self, nums):
        nums.sort()
        result = []
        n = len(nums)
        
        for i in range(n):
            # Skip duplicate values
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, n - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # Skip duplicates in left and right pointers
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        
        return result

solution = Solution()
print(solution.threeSum([-1, 0, 1, 2, -1, -4]))  
print(solution.threeSum([0, 1, 1]))              
print(solution.threeSum([0, 0, 0]))              