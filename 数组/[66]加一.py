"""
给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。 

 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。 

 你可以假设除了整数 0 之外，这个整数不会以零开头。 

 

 示例 1： 

 
输入：digits = [1,2,3]
输出：[1,2,4]
解释：输入数组表示数字 123。
 

 示例 2： 

 
输入：digits = [4,3,2,1]
输出：[4,3,2,2]
解释：输入数组表示数字 4321。
 

 示例 3： 

 
输入：digits = [0]
输出：[1]
 

 

 提示： 

 
 1 <= digits.length <= 100 
 0 <= digits[i] <= 9 
 
 Related Topics 数组 数学 👍 769 👎 0

"""

"""
模仿十进制数学计算, 只需要考虑+1后是否需要进位即可
"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        size = len(digits)
        for index in range(size - 1, -1, -1):
            if digits[index] == 9:
                digits[index] = 0
            else:
                digits[index] += 1
                break
        else:
            digits.insert(0, 1)
        return digits


# leetcode submit region end(Prohibit modification and deletion)


"""
解答成功:
执行耗时:20 ms,击败了37.93% 的Python用户
内存消耗:13 MB,击败了72.34% 的Python用户
"""
