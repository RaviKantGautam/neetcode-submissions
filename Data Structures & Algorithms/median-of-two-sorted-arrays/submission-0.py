class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        f_list = nums1+nums2
        f_list.sort()
        mid = len(f_list)//2
        if len(f_list)%2==0:
            return (f_list[:mid][-1]+f_list[mid:][0])/2
        else:
            return f_list[mid] * 1.0