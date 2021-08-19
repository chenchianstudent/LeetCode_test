# -*- coding: utf-8 -*-
"""
3Sum Closest
Medium

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

與3Sum差不多的題型和解法，給你nums和target，從nums中找出三數相加最接近target的數字並輸出。

解題思路很像3Sum這題，我先將3Sum的思路拿出來：
nums = [ -1, 0, 1, 2, -1, -4] ，我們排序過後為
nums = [ -4, -1, -1, 0, 1, 2]
接著我們固定 -4為 a。
那麼剩下的兩數(設定 b, c)相加必須為 4 (b + c = 4)
那 b和 c的位置怎麼放? 就看 a以外地方的頭跟尾 >>>>> b位置為 -1,c位置為 2
放好位置後就是判斷：
1. b+c = 1 比4小，必須要取更大的值才有辦法等於4。因此 b要向右移動一格繼續判斷。
2. 若是移動後數值比4大時，表示要取更小的值，所以我們要將c向左移一格。
3. 這樣操作後有找到解就儲存，等全部找完後一次輸出。

這題一樣我們會用到a,b,c的位置和移動概念
我們依舊會先排序，
並用for迴圈讀出第 a個值(位置)，接著就會設定 b和 c的位置 >>>> b從 a+1的位置開始 & c從陣列長度-1的地方開始

接著就是 a + b + c 與 target做比較。
等於 target：回傳 target的值即可
小於 target：代表加總值不夠大，b向右移動，找尋更大的值
大於 target：代表加總值太大，c向左移動，尋找更小的值


"""

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        min_d = None
        cloest_v = None
        
        nums.sort() # #利用sort()進行排序，這題若排序後，就會比較好解題
        
        for a in range(len(nums)):
            b = a + 1
            c = len(nums) - 1
            
            while b < c: #開始找極近值
                temp_v = nums[a] + nums[b] + nums[c]
                temp_d = target - temp_v # 三數相加的值(temp_v)，與target互減找最近值
                if temp_d <0: 
                    temp_d *= -1 #差距不存在負號
                if not min_d or (temp_d < min_d):
                    min_d = temp_d
                    cloest_v = temp_v
                    
                if temp_v > target: # 移動位置尋找
                    c -= 1
                elif temp_v < target:
                    b += 1
                elif temp_v == target:
                    return target
        return cloest_v