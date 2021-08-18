# -*- coding: utf-8 -*-
"""
Regular Expression Matching
Hard
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

Input: s = "aab", p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".

Input: s = "mississippi", p = "mis*is*p*."
Output: false

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.

有點難...我是參考這影片來做的https://www.youtube.com/watch?v=cHwEdvY8rRg&ab_channel=%E5%AE%B0%E7%9B%B8%E5%B0%8F%E7%94%98%E7%BD%97
"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(p) == 0:  # 邊界判定，都是空就True
            return (len(s) == 0)
        
        ans = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        
        # print(ans)
        ans[len(s)][len(p)] = True
        # print(len(s), len(p), ans)
        
        for i in range(len(s), -1, -1):
            for j in range(len(p) - 1, -1, -1):
                current = (i < len(s)) and ((s[i] == p[j]) or (p[j] == '.'))
                
                if j + 1 < len(p) and p[j + 1] == '*':
                    ans[i][j] = (ans[i][j + 2]) or (current and ans[i + 1][j])
                else:
                    ans[i][j] = current and ans[i + 1][j + 1]
        
                # print(i, j, ans[i][j], ans)
        return ans[0][0]