# -*- coding: utf-8 -*-
"""
4Sum
Medium

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]

*Sum的衍生型，只不過要找出陣列中相加起來的4個數字與target一樣

解題思路也是與*Sum差不多，一樣要先做排序，然後用3+1個點做尋找，因為是4Sum，所以會需要再一個點，也就會變成3+1
使用兩層 for 迴圈，綁定陣列中固定的的起始兩值（會遍歷完整個陣列，a + d）
設定 b和 c，並將起始兩值 a、 d和 b、 c做加總
加總值 > 0：將c往左走，試圖找更小總數的組合
加總值 < 0：將b往右走，試圖找更大總數的組合
加總值等於 0：此組為答案之一，若過去沒有找過這個組合的答案，即紀錄起來

"""

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Init
        results = []
        nums = sorted(nums)
        
        # Find the result
        for a in range(len(nums)):
            for d in range(a+1, len(nums)):  #這裡與3Sum不同，需要多一個迴圈進行
                b = d + 1
                c = len(nums) - 1
                temp_target = target - nums[a] - nums[d] # 先將a和d點的值減取，才會滿足b+c後所需要的值
                
                while b < c:
                    lr_sum = nums[b] + nums[c]
                    if lr_sum == temp_target:
                        result = [nums[a], nums[d], nums[b], nums[c]]
                        if result not in results:
                            results.append(result)
                        
                        b += 1
                        c -= 1
                    #老概念的位置移動
                    elif lr_sum < temp_target:
                        b += 1
                    elif lr_sum > temp_target:
                        c -= 1
        
        return results