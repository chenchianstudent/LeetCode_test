# -*- coding: utf-8 -*-
"""
String to Integer (atoi)
Medium
-----------------------------------------------------------------------------------
Input: s = "42"
Output: 42
Explanation: The underlined characters are what is read in, the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)
           ^
The parsed integer is 42.
Since 42 is in the range [-231, 231 - 1], the final result is 42.
-----------------------------------------------------------------------------------
Input: s = "   -42"
Output: -42
Explanation:
Step 1: "   -42" (leading whitespace is read and ignored)
            ^
Step 2: "   -42" ('-' is read, so the result should be negative)
             ^
Step 3: "   -42" ("42" is read in)
               ^
The parsed integer is -42.
Since -42 is in the range [-231, 231 - 1], the final result is -42.
-----------------------------------------------------------------------------------
Input: s = "4193 with words"
Output: 4193
Explanation:
Step 1: "4193 with words" (no characters read because there is no leading whitespace)
         ^
Step 2: "4193 with words" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "4193 with words" ("4193" is read in; reading stops because the next character is a non-digit)
             ^
The parsed integer is 4193.
Since 4193 is in the range [-231, 231 - 1], the final result is 4193.
-----------------------------------------------------------------------------------
Input: s = "words and 987"
Output: 0
Explanation:
Step 1: "words and 987" (no characters read because there is no leading whitespace)
         ^
Step 2: "words and 987" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "words and 987" (reading stops immediately because there is a non-digit 'w')
         ^
The parsed integer is 0 because no digits were read.
Since 0 is in the range [-231, 231 - 1], the final result is 0.
-----------------------------------------------------------------------------------
Input: s = "-91283472332"
Output: -2147483648
Explanation:
Step 1: "-91283472332" (no characters read because there is no leading whitespace)
         ^
Step 2: "-91283472332" ('-' is read, so the result should be negative)
          ^
Step 3: "-91283472332" ("91283472332" is read in)
                     ^
The parsed integer is -91283472332.
Since -91283472332 is less than the lower bound of the range [-231, 231 - 1], the final result is clamped to -231 = -2147483648.

字串中轉數字，並且有些特定規則
1.字串前後若有空字元，依舊轉換 >>>>用 str.strip() 消除空值即可。

2.有非數字字元的狀況 >>>> 若非數字字元（非正負號）是出現字首，則回傳 0 ；其他非數字字元出現在其他位置，則將字元之後全部省略。

3.一樣有overflow限制
"""

class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip() #將空白刪除
        if len(str) == 0 : #字串長度為0直接輸出0
            return 0 
			
        sign = 1
        val = 0
        if str[0] in ["-", "+"]:
            sign = 1 if str[0] == '+' else -1 #抓出正負數	
            str = str[1:] #抓出正負數後從正負符號的下一位開始做

        for i in str:
            if not i.isdigit(): #isdigit()字串是否只包含數字
                break
            val = val * 10 + (ord(i) - ord("0")) #返回ASCII對應的數值並與0相減得到實際值

        if val >= 2147483648 and sign == 1:
            return 2147483647
        elif val > 2147483648 and sign == -1:
            return -2147483648
        return val * sign
        
        '''
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        return min(INT_MAX, max(INT_MIN, val * sign))
        #^想要更快點的方法
        '''