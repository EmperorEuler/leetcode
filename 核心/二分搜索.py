"""
一个有序数组的搜索方案,
每次都使用对半分的方式, 如果搜索的目标值大于中位数, 则目标值应该在数组的右半边
如果小于中位数, 则目标值应该在数组的左半边
递归执行
我们假设该数值存在于数组中
"""


# 未完成
def binary_search(nums: [int], target: int) -> int:
    mid = len(nums) // 2
    if nums[mid] < target:
        pass
    return 0
