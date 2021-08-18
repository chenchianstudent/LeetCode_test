# -*- coding: utf-8 -*-
"""
Integer to Roman
Medium

Input: num = 3
Output: "III"

Input: num = 4
Output: "IV"

Input: num = 9
Output: "IX"

Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.

Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

輸入一串數字，將其轉換成羅馬數字
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

比較特殊的是CM = 900 ,CD = 400 有多加字母的必須減去其羅馬數字代表的值
"""

class Solution:
    def intToRoman(self, num: int) -> str:
        stl = ['M' , 'CM' , 'D' , 'CD' , 'C' , 'XC' , 'L' , 'XL' , 'X' , 'IX' , 'V' , 'IV' , 'I' ]
        nums = [1000 , 900 , 500 , 400 , 100 , 90 , 50 , 40 , 10 , 9 , 5 , 4 , 1]
        ans = ""
        
        for i ,j in enumerate(nums):
            while num >= j:
                ans += stl[i]
                num -= j
            if num == 0:
                return ans
            
'''
output解函式迴圈變化
當我輸入1994後

i,j =  (0, 1000)
ans, num =  ('M', 994)
-----
i,j =  (1, 900)
ans, num =  ('MCM', 94)
-----
i,j =  (5, 90)
ans, num =  ('MCMXC', 4)
-----
i,j =  (11, 4)
ans, num =  ('MCMXCIV', 0)
-----

當我輸入1997後
i,j =  (0, 1000)
ans, num =  ('M', 997)
-----
i,j =  (1, 900)
ans, num =  ('MCM', 97)
-----
i,j =  (5, 90)
ans, num =  ('MCMXC', 7)
-----
i,j =  (10, 5)
ans, num =  ('MCMXCV', 2)
-----
i,j =  (12, 1)
ans, num =  ('MCMXCVI', 1)
-----
i,j =  (12, 1)
ans, num =  ('MCMXCVII', 0)
-----

總而言之，就是靠python的enumerate建立索引，再利用for迴圈進行搜索，當值比索引內的數字大時，就將索引內比他小+最接近的羅馬數字加入。
enumerate()的用法
>>>seasons = ['Spring', 'Summer', 'Fall', 'Winter']
>>> list(enumerate(seasons))
[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
>>> list(enumerate(seasons, start=1))
[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]


'''