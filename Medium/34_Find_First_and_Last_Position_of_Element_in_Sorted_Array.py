# -*- coding: utf-8 -*-
"""
34. Find First and Last Position of Element in Sorted Array
Medium

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Input: nums = [], target = 0
Output: [-1,-1]

給你一個數組，找出target值的開始最左邊和最右邊的索引值，若沒有則回傳[-1, -1]

解題思路
直接想到二分法，左邊找開始的位置，當nums[mid] < target後才移動左指針，當nums[mid] <= target才向右移動左指針
然後python有二分法函式，很快就結束了。
                    

"""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = bisect.bisect_left(nums, target)
        right = bisect.bisect_right(nums, target)
        if left == right:
            return [-1, -1]
        return[left, right - 1]