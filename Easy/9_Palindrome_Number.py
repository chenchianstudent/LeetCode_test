# -*- coding: utf-8 -*-
"""
Palindrome Number
Easy

Input: x = 121
Output: true

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

簡單版的迴數，要確認負數不行
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: #負數就直接false了
            return False
        
        val = x
        y = 0
        while val: #把數字倒轉
            y = y*10 + val % 10
            val = val // 10
        return y == x #回傳是不是即可
