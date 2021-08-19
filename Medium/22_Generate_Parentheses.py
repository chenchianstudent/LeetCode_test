# -*- coding: utf-8 -*-
"""
Generate Parentheses
Medium。

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Input: n = 1
Output: ["()"]

給你n，然後把所有的()組合列出來。
有些規則要遵守：
1. "("一定先開頭
2. 一定是()這樣的組合，不會有)(的情況
3. 長度一定是 n*2

這題對我來說還蠻難想的，然後好像是大公司常考題。


我是參考這部影片的思維去寫的，28分鐘，但是有圖解思維。
https://www.youtube.com/watch?v=kXqqiGFlAus&ab_channel=%E4%BB%8A%E5%A4%A9%E6%AF%94%E6%98%A8%E5%A4%A9%E5%8E%B2%E5%AE%B3

說明一下他的想法：
1. 設置左右括弧的變數去監控規則。
2. 一組排列可能性一定是 n*2的長度，因此左右括弧相加後的數量也要是 n*2的數量。
3. 左或右括弧總數量一定為n。
4. 因為左括弧一定是開頭，在依循規則上可知，當左括弧 < n的數量時，可以先設置進去。
5. 右括弧因為有()這樣組合的規則，所以左括弧數量 < 右括弧數量時，我就要加上右括弧來形成()的組合
6. 組合有好幾種，我們要怎麼把所有的組合叫出來？ >>> 影片的重點之一，當長度已經到達 n*2後，我們就儲存並回頭至上一層查看，
   並依循規則和我們設的條件再進行新排列


"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res =[]
        
        def backtrack(s, left, right):
            if len(s) == n * 2: # 當排列組合的長度已到達n*2後，就可以將這個組合加進res[]中，否則我們繼續找排列可能性
                res.append(s)
            else:
                if left > right:    #當"("比")"多時，我們應該要加")"進去，右數量變數要加一
                    backtrack(s + ")", left, right + 1)
                if left < n:    #當"("比 n少時，我們應該要加"("進去，左數量變數要加一
                    backtrack(s + "(", left + 1, right)
        backtrack("", 0, 0) # 一開始左右數一定為0
        return res