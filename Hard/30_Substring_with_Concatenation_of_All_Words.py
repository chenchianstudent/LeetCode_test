# -*- coding: utf-8 -*-
"""
Substring with Concatenation of All Words
Hard

Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.

Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []

Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]


很難.....影片參考https://www.youtube.com/watch?v=n9fYwG3dC_Q
"""

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        result, m, n, k = [], len(s), len(words), len(words[0])
        if m < n * k:
            return result
 
        lookup = collections.defaultdict(int)
        for i in words:
            lookup[i] += 1                            

        for i in range(m+1-k*n):                    
            cur, j = collections.defaultdict(int), 0
            while j < n:                            
                word = s[i+j*k:i+j*k+k]             
                if word not in lookup: 
                    break
                cur[word] += 1
                if cur[word] > lookup[word]:
                    break
                j += 1
            if j == n:
                result.append(i)
                
        return result