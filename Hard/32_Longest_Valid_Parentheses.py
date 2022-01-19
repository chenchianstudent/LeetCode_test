# -*- coding: utf-8 -*-
"""
32. Longest Valid Parentheses
Hard

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

Input: s = ""
Output: 0

這題雖然是hard，感覺比31題還簡單....
跟之前一題差不多的概念，直接想到stack(堆疊)這個概念。


"""

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack, max_len = [-1], 0 #宣告stack 與紀錄長度的變數
        for i, j in enumerate(s):
            if j == ")":  #遇到後括弧就開始做事，沒有的話就繼續堆疊
                if stack:
                    stack.pop()
                if stack:
                    max_len = max(max_len ,i-stack[-1])
                    continue
            stack.append(i)
        return max_len