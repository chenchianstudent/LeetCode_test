# -*- coding: utf-8 -*-
"""
Valid Parentheses
Easy

Input: "()"
Output: true

Input: "()[]{}"
Output: true

Input: "(]"
Output: false

解題思路
使用stack進行，將前括號先放入stack，當遇到後括號後就把stack中最後放入的前括號拿出來做比對，相同則繼續，不相同就直接false。
值得注意的是，我們會需要多判斷"]"


"""

class Solution:
    def isValid(self, s: str) -> bool:
        pmap = {"(": ")", "[": "]", "{": "}"} #這樣就可確認是否為一致
        
        stack = []
        
        for i in s:
            if i in pmap:
                stack.append(i)
            else:
                if not stack or pmap[stack.pop()] != i: # pop()移除項目  這裡是多判斷"]"
                    return False
        return not stack