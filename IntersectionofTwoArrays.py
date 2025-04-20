class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1) & set(nums2))
        # arr = []
        # for i in range(len(nums1)):
        #     for j in range(len(nums2)):
        #         if(nums1[i]==nums2[j]):
        #             arr.append(nums1[i])
        # return list(set(arr))