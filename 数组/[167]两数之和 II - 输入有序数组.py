# 给定一个已按照 非递减顺序排列 的整数数组 numbers ，请你从数组中找出两个数满足相加之和等于目标数 target 。 
# 
#  函数应该以长度为 2 的整数数组的形式返回这两个数的下标值。numbers 的下标 从 1 开始计数 ，所以答案数组应当满足 1 <= answer[0]
#  < answer[1] <= numbers.length 。 
# 
#  你可以假设每个输入 只对应唯一的答案 ，而且你 不可以 重复使用相同的元素。 
#  
# 
#  示例 1： 
# 
#  
# 输入：numbers = [2,7,11,15], target = 9
# 输出：[1,2]
# 解释：2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
#  
# 
#  示例 2： 
# 
#  
# 输入：numbers = [2,3,4], target = 6
# 输出：[1,3]
#  
# 
#  示例 3： 
# 
#  
# 输入：numbers = [-1,0], target = -1
# 输出：[1,2]
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= numbers.length <= 3 * 10⁴ 
#  -1000 <= numbers[i] <= 1000 
#  numbers 按 非递减顺序 排列 
#  -1000 <= target <= 1000 
#  仅存在一个有效答案 
#  
#  Related Topics 数组 双指针 二分查找 👍 597 👎 0


"""
经典的两数之和的题目, 并且只有唯一答案, 更容易
简单方法: 使用两数之和的思路进行查找即可
巧妙方法: 由于这题中新增了有序数组这个特征, 由于有序数组明显会导致元素间的顺序性, 可以避免进行全量扫描
使用双指针滑动即可

"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 简单方法: 字典保存
        # rec = {}
        # index = 1
        # for num in numbers:
        #     if target - num not in rec:
        #         rec[num] = index
        #     else:
        #         return [rec[target-num], index]
        #     index += 1


        # 巧妙方法: 双指针
        l = 0
        r = len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                return [l+1, r+1]
# leetcode submit region end(Prohibit modification and deletion)

"""
简单方法:
解答成功:
执行耗时:28 ms,击败了94.96% 的Python3用户
内存消耗:15.3 MB,击败了72.35% 的Python3用户
"""


"""
巧妙方法:
解答成功:
执行耗时:40 ms,击败了44.79% 的Python3用户
内存消耗:15.3 MB,击败了65.28% 的Python3用户
"""
