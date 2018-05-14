class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        re = []
        map = {}
        for i in range(0,len(nums)):
            another = target-nums[i]
            if nums[i] in map:
                re.append(map[nums[i]])
                re.append(i)
                break
            map[another] = i
        return re

a = Solution()
re = a.twoSum([3,2,4],6)
print(re)