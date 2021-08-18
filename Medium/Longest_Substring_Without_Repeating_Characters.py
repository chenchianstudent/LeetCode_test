# -*- coding: utf-8 -*-
"""
Longest Substring Without Repeating Characters
Medium

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        str_list = [] # 宣告list
        max_length = 0 # 紀錄最大長度
        for i in s: 
            if i in str_list:  
                str_list = str_list[str_list.index(i)+1:]
                
            str_list.append(i)
            max_length = max(max_length, len(str_list)) #紀錄str_list的變化中最大值的那一次
        
        return max_length
'''
當s =  "abcabcbb"
進入函式後
if i in str_list:  
                str_list = str_list[str_list.index(i)+1:]
                
            str_list.append(i)

str_list內的資料變化為
['a']
['a', 'b']
['a', 'b', 'c']
['b', 'c', 'a']
['c', 'a', 'b']
['a', 'b', 'c']
['c', 'b']
['b']

而max_length = max(max_length, len(str_list))這段便是從上述變化中紀錄最長的那一次並輸出
'''