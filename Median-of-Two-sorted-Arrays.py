class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 = sorted(nums1+nums2)
        listlen = len(nums1)
        
        if listlen%2 is 0:
            median = (nums1[listlen//2] + nums1[(listlen//2)-1])/2
        else:
            median = nums1[math.ceil(listlen/2)-1]
        return median
