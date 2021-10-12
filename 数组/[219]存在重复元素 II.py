# 给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的 绝对值
#  至多为 k。 
# 
#  
# 
#  示例 1: 
# 
#  输入: nums = [1,2,3,1], k = 3
# 输出: true 
# 
#  示例 2: 
# 
#  输入: nums = [1,0,1,1], k = 1
# 输出: true 
# 
#  示例 3: 
# 
#  输入: nums = [1,2,3,1,2,3], k = 2
# 输出: false 
#  Related Topics 数组 哈希表 滑动窗口 👍 323 👎 0


"""
由于k规定的是最大元素间隔,　相当于判断一个ｋ大小的区间内是否存在相等的元素, 每次判断完一个区间后判断下一个k区间, 由于相邻的两个k区间之间只有
一个元素差异, 所以可以单独这个差别元素单独剔除, 新增新元素, 即可最低消耗地变更了整个区间
注意: k是索引差值, 比如k=2, 即索引差值为2, 如0和2, 所以其实k区间中包含了k+1个元素
为了快速判断是否存在元素, 使用set或者字典
"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        rec = set()
        last_value_index = 0
        for num in nums[:k+1]:
            if num in rec:
                return True
            rec.add(num)
        if k > len(nums)-1:
            return False
        for num in nums[k+1:]:
            rec.remove(nums[last_value_index])
            if num in rec:
                return True
            rec.add(num)
            last_value_index += 1
        return False

# leetcode submit region end(Prohibit modification and deletion)


"""
解答成功:
执行耗时:96 ms,击败了38.98% 的Python3用户
内存消耗:22.6 MB,击败了99.46% 的Python3用户
"""
