# -*- coding: utf-8 -*-
"""
31. Next Permutation
Medium

Input: nums = [1,2,3]
Output: [1,3,2]

Input: nums = [3,2,1]
Output: [1,2,3]

Input: nums = [1,1,5]
Output: [1,5,1]

Input: nums = [1]
Output: [1]

找出數組中第二個大的數，若沒有則有逆序排列。

這題小難，但是是有規則的。爬了幾篇文章，規則思路大同小異

給你一個數組
1　2　7　4　3　1
下一個排列：

1　3　1　2　4　7
比較後可以知道，2後面的數字都是降序排列的，我們只需要把2後面比2大放入做交換即可，最後再升序排列。

數組中7開始降序排列，那就表示7431已經無法透過排序找到更大的數字(因為7已經是最大數)。
如果要得到第二大數組，我們只能去動2這個位置，而且只能换成比2大的數字。
數字替換的限制，我們需要換成剛好比2大且是2後面的數字，我們就可以使用反證法來說明換成其他數比當前數字小，又或是大於正確的next

解題思路
1. 先從數組最右邊開始搜尋，若是第 i個值比 i+1個值小，那就讓 i往右側找比第i個值大的值當最小值
2. 找到後交換第 i 個值以及比第 i 個值大的最小值

"""

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        min_v = 101  #設置此變數是用來篩題目限制的，0 <= nums[i] <= 100
        min_p = -1
        p = -1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                p = i
                for j in range(i, len(nums)):
                    if nums[i] < nums[j] < min_v:
                        min_v = nums[j]
                        min_p = j               
                break        
        # Sort
        if p == -1:
            nums.sort()
        else:
            nums[i], nums[min_p] = nums[min_p], nums[i]            
            for j in range(i+1, len(nums)-1): #氣泡排序
                for k in range(i+1, len(nums)-1):
                    if nums[k] > nums[k+1]:
                        nums[k], nums[k+1] = nums[k+1], nums[k]  
              
        