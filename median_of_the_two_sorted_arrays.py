class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        m, n = len(nums1), len(nums2)
        imin, imax = 0, m
        half_len = (m + n + 1) // 2
        
        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i
            
            if i < m and nums1[i] < nums2[j - 1]:
                imin = i + 1  # i is too small
            elif i > 0 and nums1[i - 1] > nums2[j]:
                imax = i - 1  # i is too big
            else:
                # i is perfect
                if i == 0: max_left = nums2[j - 1]
                elif j == 0: max_left = nums1[i - 1]
                else: max_left = max(nums1[i - 1], nums2[j - 1])
                
                if (m + n) % 2 == 1:
                    return max_left
                
                if i == m: min_right = nums2[j]
                elif j == n: min_right = nums1[i]
                else: min_right = min(nums1[i], nums2[j])
                
                return (max_left + min_right) / 2.0

solution = Solution()
print(solution.findMedianSortedArrays([1, 3], [2]))         
print(solution.findMedianSortedArrays([1, 2], [3, 4]))      
