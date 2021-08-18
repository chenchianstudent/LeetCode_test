# -*- coding: utf-8 -*-
"""
Longest Palindromic Substring
Medium

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Input: s = "cbbd"
Output: "bb"

Input: s = "a"
Output: "a"

從字串中找出迴文，輸出要是最大長度的迴文。
解題注意
奇數量迴文是透過中間數字往左右發展尋找迴文的，思考邏輯應該從中間為起點進行設置，再向外尋找。
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        #先將單字這種的迴文先做if篩出並輸出
        if (len(s) <= 1) or s == s[::-1]: # [::-1]意思為順序相反 ex.a =[1,2,3] b=a[::-1] >>> b=[3,2,1]
            return s
        else:
            maxlen = 1 # 迴文最大的長度
            start = 0 #迴文開始的位置
            for i in range(1 , len(s)):
            # 跑第一圈時，odd要找 s[-1:2]，event要找 s[0:2]
            #odd因為是取奇數量，所以他需要左右擴展尋找，因此從字串開頭找起時，往左會到-1的位置
            # 跑第二圈時，odd要找 s[0:3]，event要找 s[1:3]
            # 跑第三圈時，odd要找 s[1:4]，event要找 s[2:4]
                odd = s[i - maxlen - 1 : i+1]
                even = s[i - maxlen : i+1]
                #判斷是否為迴文的if迴圈，分別對odd和even著手
                if i - maxlen - 1 >= 0 and odd == odd[::-1]: #若是迴文的話odd就算[::-1]字串也要相同
                    start = i - maxlen -1 #紀錄新的迴文位置
                    maxlen += 2
                elif i - maxlen >= 0 and even == even[::-1]:
                    start = i-maxlen
                    maxlen += 1
        return s[start : start + maxlen]