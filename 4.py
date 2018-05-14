class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        res = sorted(nums2+nums1)
        return self.midnumber(res,0,len(res)-1)

    def midnumber(self,nums,start,end):
        if (end-start)%2 == 0:
            mid=int((start+ end)/2)
            return  nums[mid]
        else :
            mid = int((start+ end)/2)
            re =  (nums[mid]+nums[mid+1])/2
            return re
nums1 = [1,3]
nums2 = [2]
a = Solution()
re = a.findMedianSortedArrays(nums1,nums2)
print(re)