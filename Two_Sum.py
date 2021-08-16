# -*- coding: utf-8 -*-
"""
Two Sum
Easy

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
"""
#透過map的方式將時間複雜度O(N^2)降為O(N)，在python當中我們可以利用dictionary進行資料儲存 ex.d = {key1: value1, key2: value2}
class Solution(object):
    def twoSum(self, nums, target):
        numMap = {}  # 創建dictionary
        for i in range(len(nums)): #利用for迴圈搜尋符合target - nums中符合的數字
            if numMap.__contains__(target - nums[i]):
                return[numMap.get(target - nums[i]), i]
            else:
                numMap[nums[i]] = i #沒找到就下一把