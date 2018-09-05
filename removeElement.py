class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while val in nums:
            nums.remove(val)
     #不用想的太复杂。先想想伪代码。
     #如果有值为val的元素在nums中，则在nums中移除。
     #明白remove ,del ,pop 的区别。
     #remove():删除首个符合条件的元素,按值删除。如remove(2),意为删除列表中值为2的首个元素。
     #del:根据索引（元素所在位置）来删除的。如 del list[1]
     #pop(obj):按位删除(根据索引删除).删除时会返回被删除的元素。obj:可选参数，要移除列表元素的索引值，不能超过列表总长度，默认为 index=-1，删除最后一个列表值。
