# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target 的那 两个 整数，并返回它们的数组下标。 
# 
#  你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。 
# 
#  你可以按任意顺序返回答案。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [2,7,11,15], target = 9
# 输出：[0,1]
# 解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [3,2,4], target = 6
# 输出：[1,2]
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [3,3], target = 6
# 输出：[0,1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= nums.length <= 10⁴ 
#  -10⁹ <= nums[i] <= 10⁹ 
#  -10⁹ <= target <= 10⁹ 
#  只会存在一个有效答案 
#  
# 
#  进阶：你可以想出一个时间复杂度小于 O(n²) 的算法吗？ 
#  Related Topics 数组 哈希表 👍 12314 👎 0

"""
使用字典来保存{数值: index}, 从第一个数字开始, 先读取当前数值和target的差值, 就可以找出能与当前数值组合和为target的数值是多少,
然后查找字典中是否有该数值, 如果有那么说明在读取过的数值中, 有一个数和当前的数组合和为target, 这两个数值即为答案, 注意提交的是index
由于计算过程中不能用当前数值和自己求和, 所以计算过程结束后才可以把当前数值存入字典
由于只存有一个有效答案, 所以求得一个答案后可以直接结束
"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        rec = {}
        index = 0
        for num in nums:
            if target - num in rec:
                return [rec[target - num], index]
            rec[num] = index
            index += 1


# leetcode submit region end(Prohibit modification and deletion)


"""
解答成功:
执行耗时:20 ms,击败了82.69% 的Python用户
内存消耗:13.8 MB,击败了51.09% 的Python用户
"""
