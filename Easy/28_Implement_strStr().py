# -*- coding: utf-8 -*-
"""
Implement strStr()
Easy

Input: haystack = "hello", needle = "ll"
Output: 2

Input: haystack = "aaaaa", needle = "bba"
Output: -1

Input: haystack = "", needle = ""
Output: 0


"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle) #find()完成這題..... find()如果沒找到子串的話就會回傳-1