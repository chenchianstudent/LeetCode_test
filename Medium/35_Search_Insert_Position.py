# -*- coding: utf-8 -*-
"""
35. Search Insert Position
Easy

Input: nums = [1,3,5,6], target = 5
Output: 2

Input: nums = [1,3,5,6], target = 2
Output: 1

Input: nums = [1,3,5,6], target = 7
Output: 4

Input: nums = [1,3,5,6], target = 0
Output: 0

Input: nums = [1], target = 0
Output: 0

給一個陣列和target，找出target在這個陣列的位置，若沒有找到則回傳應插入的位置。

解題思路
這題考二元搜索法(Binary Search)

先找出中間值 m，m左邊的數必然小於 m，反之m右邊的數必然大於 m。
接著就能與target做比較：
1. target == m，那 m所在的位置就是我們要的答案。
2. target > m，表示答案只可能在 m右邊到尾端之間(不含m)。
3. target < m，表示答案只可能在 m左邊到開頭之間(不含m)。
這樣當每次取得 m值，並和target做比較，則可以見少至少一半可能的數量，直到target == m。


"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        m = (l + r) // 2
        while l <= r:
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
            m = (l + r) // 2
        return l