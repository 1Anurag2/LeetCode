class Solution:
    def peakElement(self, arr):
        n = len(arr)
        low = 0
        high = n - 1

        while low <= high:
            mid = (low + high) // 2

            left = arr[mid - 1] if mid > 0 else float('-inf')
            right = arr[mid + 1] if mid < n - 1 else float('-inf')

            if arr[mid] > left and arr[mid] > right:
                return mid  # Found a peak

            elif arr[mid] < right:
                low = mid + 1  # Move right

            else:
                high = mid - 1  # Move left

        

sol = Solution()
print(sol.peakElement([1, 2, 4, 5, 7, 8, 3]))
print(sol.peakElement([10, 20, 15, 2, 23, 90, 80]))
print(sol.peakElement( [1, 2, 3]))
print(sol.peakElement( [10, 2, 3]))
