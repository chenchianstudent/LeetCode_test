# -*- coding: utf-8 -*-
"""
3Sum
Medium

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Input: nums = []
Output: []

Input: nums = [0]
Output: []


從nums中找出相加為0的三個數。此外這三數不能重複使用(位置)

**解題思路**
這題排序後會比較好想和好解！
nums = [ -1, 0, 1, 2, -1, -4] ，我們排序過後為
nums = [ -4, -1, -1, 0, 1, 2]
接著我們固定 -4為 a。
那麼剩下的兩數(設定 b, c)相加必須為 4 (b + c = 4)
那 b和 c的位置怎麼放? 就看 a以外地方的頭跟尾 >>>>> b位置為 -1,c位置為 2
放好位置後就是判斷：
1. b+c = 1 比4小，必須要取更大的值才有辦法等於4。因此 b要向右移動一格繼續判斷。
2. 若是移動後數值比4大時，表示要取更小的值，所以我們要將c向左移一格。
3. 這樣操作後有找到解就儲存，等全部找完後一次輸出。

"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums)<3 : return [] #解決例外
        
        nums.sort() #利用sort()進行排序，這題若排序後，就會比較好解題
        res = set() #set()建立空的集合，用來儲存輸出的答案用的
        
        for i,j in enumerate(nums[:-2]):
            if i >= 1 and j == nums[i-1]: #確保i和j指向的位置沒有重複
                continue
            d={}
            for x in nums[i+1:]:
                if x not in d:
                    d[-j-x] = 1
                else:
                    res.add((j,-j-x,x))
        return list(res)
        