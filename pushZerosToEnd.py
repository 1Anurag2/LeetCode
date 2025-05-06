class Solution:
	def pushZerosToEnd(self,arr):
		element_list = []
		count_Zero = arr.count(0)
		zero_list = [0] * count_Zero
		for value in arr:
			if (value != 0):
				element_list.append(value)
		result = element_list + zero_list
		return result
				
sol = Solution()
print(sol.pushZerosToEnd([1, 2, 0, 4, 3, 0, 5, 0]))
print(sol.pushZerosToEnd([10, 20, 30]))
    	        