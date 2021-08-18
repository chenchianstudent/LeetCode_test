# -*- coding: utf-8 -*-
"""
Container With Most Water
Medium

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Input: height = [1,1]
Output: 1

Input: height = [4,3,2,1,4]
Output: 16

Input: height = [1,2,1]
Output: 2

給你一個數陣列，將陣列的數字以長條圖展示，並把這些長條想成木板，計算兩木板間能裝多少水，求出最大容積。

"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height)-1
        
        while left < right:
            # 主要計算容積
            temp = min(height[left], height[right]) * (right - left) # 計算容積 長(找出兩柱間最小值)*寬
            max_area = max(temp ,max_area) # 與先前的容積做比對，最大的留著
            
            # 哪邊的高度小，那小的那邊就該移動，找出更好容積
            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                left += 1
                right -= 1
        return max_area