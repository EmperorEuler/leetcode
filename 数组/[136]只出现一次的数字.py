# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。 
# 
#  说明： 
# 
#  你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？ 
# 
#  示例 1: 
# 
#  输入: [2,2,1]
# 输出: 1
#  
# 
#  示例 2: 
# 
#  输入: [4,1,2,1,2]
# 输出: 4 
#  Related Topics 位运算 数组 👍 2058 👎 0


"""
简单思路:把出现过的数字用set存起来, 再次出现时删除, 最后剩下的就是目标
巧妙的思路:使用异或, 由于异或会导致相同的数字结果为0, 所以成对出现的数字结果为0
最终剩下不成对的数字就是最终结果
"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 简单方法
        # rec = set()
        # for num in nums:
        #     if num not in rec:
        #         rec.add(num)
        #     else:
        #         rec.remove(num)
        # return rec.pop()

        # 巧妙方法
        rec = 0
        for num in nums:
            rec ^= num
        return rec

# leetcode submit region end(Prohibit modification and deletion)


"""
# 简单方法
解答成功:
执行耗时:44 ms,击败了50.68% 的Python3用户
内存消耗:16.8 MB,击败了6.15% 的Python3用户
"""


"""
# 巧妙方法
解答成功:
执行耗时:32 ms,击败了96.48% 的Python3用户
内存消耗:16.4 MB,击败了97.61% 的Python3用户
"""
