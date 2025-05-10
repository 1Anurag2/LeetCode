class Solution:
    def binarySearch(self,arr:list[int],target) -> int:
        # arr.sort()     it's work only upon sorted array
        n = len(arr)
        start = 0
        end = n-1
        
        while end >= start:
            mid = (start + end) // 2

            if arr[mid] < target:
                start = mid + 1
            elif arr[mid] > target:
                end = mid - 1
            else:
                return mid
        return -1

sol = Solution()
list1 = [2, 3, 3, 4, 5, 6, 7, 8, 9, 21, 34, 56]
print(sol.binarySearch(list1,3))
