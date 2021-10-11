"""
给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。 

 请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。 

 注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。为了应对这种情况，nums1 的初始长度为 m + n，其中前 m 个元素表示应合并的元
素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n 。 

 

 示例 1： 

 
输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
输出：[1,2,2,3,5,6]
解释：需要合并 [1,2,3] 和 [2,5,6] 。
合并结果是 [1,2,2,3,5,6] ，其中斜体加粗标注的为 nums1 中的元素。
 

 示例 2： 

 
输入：nums1 = [1], m = 1, nums2 = [], n = 0
输出：[1]
解释：需要合并 [1] 和 [] 。
合并结果是 [1] 。
 

 示例 3： 

 
输入：nums1 = [0], m = 0, nums2 = [1], n = 1
输出：[1]
解释：需要合并的数组是 [] 和 [1] 。
合并结果是 [1] 。
注意，因为 m = 0 ，所以 nums1 中没有元素。nums1 中仅存的 0 仅仅是为了确保合并结果可以顺利存放到 nums1 中。
 

 

 提示： 

 
 nums1.length == m + n 
 nums2.length == n 
 0 <= m, n <= 200 
 1 <= m + n <= 200 
 -10⁹ <= nums1[i], nums2[j] <= 10⁹ 
 

 

 进阶：你可以设计实现一个时间复杂度为 O(m + n) 的算法解决此问题吗？ 
 Related Topics 数组 双指针 排序 👍 1140 👎 0

"""

"""
该题目的核心是把两个数组合并并排序
由于两个数组之前是有序的, 所以在同一个数组内部并不需要考虑大小的问题
重点在于比较两个数组间的大小比较
由于题目并没有强制要求原地排序, 分别顺序遍历两个数组, 每次找到偏小的数值进行填充即可
"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        size = len(nums1)
        res = [0] * size
        if m < 1:
            for i in range(size):
                nums1[i] = nums2[i]
            return
        if n < 1:
            return
        l = 0
        r = 0
        for i in range(size):
            if l == m:
                # 这种情况说明nums1数组已经读完但是nums2数组还没有读完
                i2 = i
                tmp = n
                while r < tmp:
                    res[i2] = nums2[r]
                    r += 1
                    i2 += 1
                break
            if r == n:
                # 这种情况说明nums2数组已经读完但是nums1数组还没有读完
                i2 = i
                tmp = m
                while l < tmp:
                    res[i2] = nums1[l]
                    print("i2", i2, "l", l)
                    l += 1
                    i2 += 1
                break
            if nums1[l] < nums2[r]:
                res[i] = nums1[l]
                l += 1
            else:
                res[i] = nums2[r]
                r += 1
        for i in range(size):
            nums1[i] = res[i]


# leetcode submit region end(Prohibit modification and deletion)


"""
解答成功:
执行耗时:16 ms,击败了73.96% 的Python用户
内存消耗:13.1 MB,击败了40.24% 的Python用户
"""
