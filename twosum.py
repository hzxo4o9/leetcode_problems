class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0,len(nums)-1):
            c = target - nums[i]
            j=i+1
            nums1 = nums[j:]
            if c in nums1:
                return [i,nums1.index(c)+j]
            else:continue
