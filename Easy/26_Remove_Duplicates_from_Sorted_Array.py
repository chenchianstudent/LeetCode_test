# -*- coding: utf-8 -*-
"""
Remove Duplicates from Sorted Array
Easy

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

這題有個限制，就是需要in-place algorithm。
in-place >>>> 所有的操作修改，除了一些計數用的變數外，都是在原本的資料結構上處理解決，像這題就是完全只有操作原陣列。
如果沒有此限制的話，我們可能就會像之前一樣宣告新的ArrayList，然後將不重複的數加進尾端，最後將其轉為Array。
這題其實就在考減少空間複雜度，那想當然的，時間複雜度會偏低。
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0 #排出例外
        i, j = 0, 1 #i記錄目前存放至哪個位置，j則是完整遍歷整個陣列，以利尋找不重複的數字
        
        while j <len(nums):  #當發現有不同的數字後，就將j的數字放到i的位置，再繼續下去
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
            j += 1
        return i + 1