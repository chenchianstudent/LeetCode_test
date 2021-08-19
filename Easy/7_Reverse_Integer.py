# -*- coding: utf-8 -*-
"""
Reverse Integer
Easy

Input: x = 123
Output: 321

Input: x = -123
Output: -321

Input: x = 120
Output: 21

Input: x = 0
Output: 0

only store integers within the 32-bit signed integer range: [−2³¹, 2³¹ − 1]

數字反轉，且要注意0在前面要自動消除以及正負數
另外，要注意only store integers within the 32-bit signed integer range: [−2³¹, 2³¹ − 1]

"""

class Solution:
    def reverse(self, x: int) -> int:
        if x == 0: #如果數字是0就直接輸出
            return 0
        
        ans = str(x)
        #if判斷正負數
        if x > 0:
            ans = int(ans[::-1]) #直接用python的語法倒過來即可
        else:
            ans = int(ans[:0:-1])*-1
        #causes the value to go outside the signed 32-bit integer range  [−2³¹, 2³¹ − 1], then return 0.  <-----解決這個問題 2^31-1 我直接乘開來放置減少計算    
        if 2147483647 > ans > -2147483648: 
            return ans
        else:
            return 0