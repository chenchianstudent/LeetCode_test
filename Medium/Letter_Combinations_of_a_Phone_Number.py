# -*- coding: utf-8 -*-
"""
Letter Combinations of a Phone Number
Medium

這題是看圖施工，所以我先貼網址https://leetcode.com/problems/letter-combinations-of-a-phone-number/
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Input: digits = ""
Output: []

Input: digits = "2"
Output: ["a","b","c"]

輸入數字，我們會依循圖片內的數字與英文字母規則找到所有的組合

有點像以前按鍵式手機的鍵盤
"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "": return [] # 把特殊情況篩掉
        
        # 建立圖片上按鍵的map
        phmap = {'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
        # 建立輸出的陣列
        res = [""]
        
        for i in digits: 
            res = [a + b for b in phmap[i] for a in res]
        return res