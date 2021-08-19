# -*- coding: utf-8 -*-
"""
13. Roman to Integer
Easy

Input: s = "III"
Output: 3

Input: s = "IV"
Output: 4

Input: s = "IX"
Output: 9

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


"""

class Solution:
    def romanToInt(self, x: str) -> int:
        result = 0;
        map = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}   #直接map出來所有符號與對應的數字
        for i in range(len(x)):                                      
            if(map[x[i]]):                                           #防呆
                temp = map[x[i]];
                if(i != 0 and map[x[i-1]] < map[x[i]]):              #如果不是第一個且前一個數值比當前值小
                    temp = temp - (map[x[i-1]])*2;                   #就減掉 X2 是因為我下一段不管怎樣會先加進去了 所以減兩次
                result = result + temp ;
        return  result;