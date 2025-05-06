class Solution:
    def twoSum(self, nums, target):
       for i in range(len(nums)):
           for j in range(i+1,len(nums)):
               if(nums[i]+nums[j] == target):
                    return [i,j]


sol = Solution()
         
print(sol.twoSum([2,5,5,11], 10))          




# class Solution:
#     def twoSum(self, nums, target):
#         num_to_index = {} 
        
#         for i, num in enumerate(nums):  
#             complement = target - num  
#             if complement in num_to_index:  
#                 return [num_to_index[complement], i]  
#             num_to_index[num] = i  

# sol = Solution()
# print(sol.twoSum([2, 7, 11, 15], 9))  
# print(sol.twoSum([3, 2, 4], 6))      
# print(sol.twoSum([3, 3], 6))          
