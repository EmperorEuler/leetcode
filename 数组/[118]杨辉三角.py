# 给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。 
# 
#  在「杨辉三角」中，每个数是它左上方和右上方的数的和。 
# 
#  
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: numRows = 5
# 输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
#  
# 
#  示例 2: 
# 
#  
# 输入: numRows = 1
# 输出: [[1]]
#  
# 
#  
# 
#  提示: 
# 
#  
#  1 <= numRows <= 30 
#  
#  Related Topics 数组 动态规划 👍 600 👎 0


"""
观察规律：先生成对应行数, 行首和行末都是1, 依然用上一行的两个邻位求和填充最新的空格
"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        cnt = 1
        while cnt <= numRows:
            res.append([1] * cnt)
            cnt += 1
        for i in range(2, numRows):
            for i2 in range(1, i):
                res[i][i2] = res[i-1][i2-1] + res[i-1][i2]
        return res
# leetcode submit region end(Prohibit modification and deletion)


"""
解答成功:
执行耗时:40 ms,击败了11.20% 的Python3用户
内存消耗:14.7 MB,击败了97.27% 的Python3用户
"""
