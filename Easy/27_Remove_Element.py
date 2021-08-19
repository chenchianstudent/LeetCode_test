# -*- coding: utf-8 -*-
"""
Remove Element
Easy

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).

給你數組和一個數字，找出數組中與數字不同的值。
但是要注意的是：
1. 只能修改該數組，空間複雜度最多為 1(不能創建新的數組去儲存)
2. 可以不管超過回傳值以後nums的值


"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j= 0
        for i in nums:   #比我想像中的簡單
            if i != val:
                nums[j] = i
                j += 1
        return j
        