# -*- coding: utf-8 -*-
"""
Divide Two Integers
Medium

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = truncate(-2.33333..) = -2.

Input: dividend = 0, divisor = 1
Output: 0

Input: dividend = 1, divisor = 1
Output: 1

計算兩數相除的商。但是不可使用乘法、除法和mod運算。

解題思路
使用移位操作代替乘法。
1. 被除數/除數 = 商  >>> 被除數 = 除數 * 商
2. 商可以表示為 a0 * 2^0 + a1 * 2^1 + … + ai * 2^i + … + an * 2^n.
3. python中左移操作"<<" = 一個數 * 2，反之右移 = 一個數 / 2
4. 執行除數左移直到大於被除數，尋找解答。
   ex.28/3，會執行三次左移，使3 * 2 * 2 * 2 = 3 * 8 = 24 < 28(注意四次左移操作得到3 * 2^4 = 48 > 28).紀錄2 * 2 * 2= 2^3 = 8.
5. 讓 28 - 24 得到 4，然後像第四步一樣計算 4/3， 3*2^0 = 3<4 >>>2^0 = 1
6. 因為 4 - 3 = 1小於 3，我們就會停止計算。將前面的2 ^3 加上 1 >>> 8 + 1 = 9 ，也就是我們答案商


"""

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        res, flag = 0, 1
        if(dividend < 0 and divisor > 0)or(dividend > 0 and divisor < 0): # 設定正負號
            flag = -1
        
        dividend = abs(dividend) #abs()絕對值
        divisor = abs(divisor)
        
        while(dividend >= divisor):   
            n = 0
            while(dividend >= divisor << n):  # "<<"左移操作 = 一個數乘2。反之，右移除以2
                n += 1
            res += 1 << (n-1)
            dividend -= (divisor << (n-1))
        
        ans  = res * flag # 值 * 正負號
        
        if ans >= 2147483647: # MAX&　MIN 判斷
            return 2147483647
        elif ans <= -2147483648:
            return -2147483648
        else:
            return res * flag
            