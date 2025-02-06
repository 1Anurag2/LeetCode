from collections import defaultdict

class Solution:
    def tupleSameProduct(self, nums):
        product_count = defaultdict(int)
        n = len(nums)
        count = 0
        
        
        for i in range(n):
            for j in range(i + 1, n):
                product = nums[i] * nums[j]
                product_count[product] += 1
        
        
        for freq in product_count.values():
            if freq > 1:
                count += 8 * (freq * (freq - 1) // 2)
        
        return count


sol = Solution()
print(sol.tupleSameProduct([2,3,4,6]))  
print(sol.tupleSameProduct([1,2,4,5,10]))  
