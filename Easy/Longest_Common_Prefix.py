# -*- coding: utf-8 -*-
"""
Longest Common Prefix
Easy

Input: strs = ["flower","flow","flight"]
Output: "fl"

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

找出相同的字符
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""  #防呆，確保輸入的字串是有東西的
        s1 = min(strs)
        s2 = max(strs)
        
        for i, j in enumerate(s1):
            if j != s2[i]:  #當比對時已經沒有相同的字符，我就輸出當前比對的字符了
                return s1[:i]
        return s1        