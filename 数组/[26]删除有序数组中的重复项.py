# 给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。 
# 
#  不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。 
# 
#  
# 
#  说明: 
# 
#  为什么返回数值是整数，但输出的答案是数组呢? 
# 
#  请注意，输入数组是以「引用」方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。 
# 
#  你可以想象内部操作如下: 
# 
#  
# // nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
# int len = removeDuplicates(nums);
# 
# // 在函数里修改输入数组对于调用者是可见的。
# // 根据你的函数返回的长度, 它会打印出数组中 该长度范围内 的所有元素。
# for (int i = 0; i < len; i++) {
#     print(nums[i]);
# }
#  
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,1,2]
# 输出：2, nums = [1,2]
# 解释：函数应该返回新的长度 2 ，并且原数组 nums 的前两个元素被修改为 1, 2 。不需要考虑数组中超出新长度后面的元素。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [0,0,1,1,1,2,2,3,3,4]
# 输出：5, nums = [0,1,2,3,4]
# 解释：函数应该返回新的长度 5 ， 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4 。不需要考虑数组中超出新长度后面的元素。
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= nums.length <= 3 * 10⁴ 
#  -10⁴ <= nums[i] <= 10⁴ 
#  nums 已按升序排列 
#  
# 
#  
#  Related Topics 数组 双指针 👍 2256 👎 0

"""
此处虽然返回的是数值而不是列表, 但是由于python中列表是引用传递的, 作为参数传递给函数的列表, 在函数内部被修改, 改动被保留
所以只需要返回有效内容的数值N, 取列表的前N个元素, 即为目标的列表
由于要求是原地修改, 所以应该考虑在记录当前元素的数值, 如果下一个数值和当前数值相同, 则说明下一个索引的数值应该被删除, 把该索引预留
等待遇到不同数值的数时把该索引填满, 再进入下一个数值
"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1:
            return 0
        last_value = nums[0] - 1
        l = 0  # 可填充的索引位置
        r = 0
        size = len(nums)
        # 由于需要边读取边修改列表, 所以不应该使用遍历列表, 而是读取列表的每个index
        for r in range(size):
            if last_value != nums[r]:
                last_value = nums[r]
                nums[l] = last_value
                l += 1
        return l


# leetcode submit region end(Prohibit modification and deletion)


"""
解答成功:
执行耗时:20 ms,击败了89.78% 的Python用户
内存消耗:14.2 MB,击败了31.38% 的Python用户
"""
