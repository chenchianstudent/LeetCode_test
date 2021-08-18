# -*- coding: utf-8 -*-
"""
ZigZag Conversion
Medium

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

指定row來將字串重新排放，並以Z字寫法放置，而非從頭開始放置
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: #先將單字串篩掉
            return s
        #透過numRows的設定去宣告空字串儲存
        strings = ['' for r in range(numRows)]
        row = 0; #宣告字串設置的位置
        step = 1; #宣告字串設置的層數
        
        for i in s:
            strings[row] += i
            if row == numRows-1: #當row到達指定行數的最尾端，我們就要翻轉step，讓他能繼續從尾巴再向頭填
                step = -1
            elif row == 0: #當row又從尾巴填到頭後，我們就再次翻轉step，讓他能從起點再開始填到尾巴
                step = 1
            row += step #row要跟step做更新
        return ''.join(strings) 將字串合併起來
            
"""
圖解該題
ABCDEFG

0 ''  step = 0
1 ''  row = 0
2 ''  row +=step

BCDEFG

0 'A'  step = 1
1 ''  row = 0
2 ''  row +=step

CDEFG

0 'A'  step = 1
1 'B'  row = 1
2 ''  row +=step

DEFG

0 'A'  step = 1
1 'B'  row = 2
2 'C'  row +=step

到邊界後進行step翻轉  1>>>-1

EFG

0 'A'  step = -1
1 'BD'  row = 1
2 'C'  row +=step

FG

0 'AE'  step = -1
1 'BD'  row = 0
2 'C'  row +=step

到邊界後進行step翻轉  -1>>>1

G

0 'A E'  step = 1
1 'BDF'  row = 1
2 'C'  row +=step


0 'A E'  step = 1
1 'BDF'  row = 2
2 'C G'  row +=step

最後將 0,1,2的字串串連起來即可輸出

"""
