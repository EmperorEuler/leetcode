# 给定一个整数数组，判断是否存在重复元素。 
# 
#  如果存在一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: [1,2,3,1]
# 输出: true 
# 
#  示例 2: 
# 
#  
# 输入: [1,2,3,4]
# 输出: false 
# 
#  示例 3: 
# 
#  
# 输入: [1,1,1,3,3,4,3,2,4,2]
# 输出: true 
#  Related Topics 数组 哈希表 排序 👍 501 👎 0


"""
使用set来保存出现过的值, 查找是否有保存过
"""

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        rec = set()
        for num in nums:
            if num in rec:
                return True
            rec.add(num)
        return False
# leetcode submit region end(Prohibit modification and deletion)


"""
解答成功:
执行耗时:36 ms,击败了74.83% 的Python3用户
内存消耗:19.6 MB,击败了44.89% 的Python3用户
"""
