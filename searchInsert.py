class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #第一种情况：目标值在数组中，则返回索引
        if target in nums:
            return nums.index(target)
        #第二种情况：不在且插入位置在数组中间
        if target not in nums:
            for i in range(len(nums)):
                if target < nums[i]:
                    return i
                else:
                    pass
        #第三种：前面两种都不是，即为目标值比nums中的任何一个值都要大，则插入位置在末尾
        if (target > nums[len(nums)-1]):
            return len(nums)
        
                
