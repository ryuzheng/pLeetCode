#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
# https://leetcode-cn.com/problems/two-sum/description/
#
# algorithms
# Easy (45.09%)
# Total Accepted:    271.9K
# Total Submissions: 603K
# Testcase Example:  '[2,7,11,15]\n9'
#
# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
#
# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
#
# 示例:
#
# 给定 nums = [2, 7, 11, 15], target = 9
#
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
#
#
#
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for x in range(0, len(nums)):
        #     for y in range(x + 1, len(nums)):
        #         if nums[x] + nums[y] == target:
        #             return [x, y]
        # return None
        new_list = {}
        for index, num in enumerate(nums):
            minus = target - num
            if minus in new_list:
                return [index, new_list[minus]]
            new_list[num] = index
        return None
