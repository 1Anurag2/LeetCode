class Solution:
    #User function Template for python3
    #Function to count inversions in the array.
    def inversionCount(self, arr):
        count = 0
        for i in range(len(arr)-1):
            for j in range(i+1,len(arr)):
                if (arr[i]>arr[j]):
                    count += 1
                    
        return count
sol =  Solution()
arr = [57, 38 ,91 ,10 ,38, 28 ,79 ,41]
arr1 = [2, 4, 1, 3, 5]
print(sol.inversionCount(arr))
print(sol.inversionCount(arr1))