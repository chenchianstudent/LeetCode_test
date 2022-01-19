# -*- coding: utf-8 -*-
"""
33. Search in Rotated Sorted Array
Medium

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Input: nums = [1], target = 0
Output: -1

題目給的例子和說明有點少，沒有太多例子可以去做更細的思考...
[0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

找出旋轉有序數組中是否有包含我們所設定的值，有則回傳序號，沒有則回傳-1

解題思路
直接想到二分法。
利用左邊、右邊和中間，判斷查找的target是在mid的左還右。
假設數組為 A，左邊為l，右邊為r，中間為m
1. 如果target == A[m] 直接回傳結果
2. 若 A[m]<A[r]，代表 m到 r是有序的，這時只需要判斷target是否在m到r之間，
   是的話左邊移到 m+1，否則就target在另一半，即把右邊移到 m-1。
3. 若 A[m]>=A[r]，代表從 l到m是有序的，只需要判斷target是否在範圍内，對應移動邊界即可


"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l<= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[l] <= nums[m] < target or \
                 target < nums[l] <= nums[m] or \
                 nums[m] < target < nums[l]:
                        l = m + 1
            else:
                r = m - 1
        return -1