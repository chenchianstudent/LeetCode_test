# -*- coding: utf-8 -*-
"""
Median of Two Sorted Arrays
Hard

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

這題我參考該網址https://blog.csdn.net/CSerwangjun/article/details/89815121
原理就是尋找2分法的規則，同時還要處裡邊界問題
難在時間複雜度上
"""


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lenA = len(nums1)
        lenB = len(nums2)
        if lenA > lenB: # 調整長度
            nums1,nums2,lenA,lenB = nums2,nums1,lenB,lenA
        imin,imax = 0,lenA,
        mid = int((lenA+lenB)/2) #取中位數
        
        while imin <= imax:
            i = int((imin+imax)/2)
            j = mid-i
            if i < lenA and nums1[i] < nums2[j-1]:
                imin=i+1
            elif 0 < i and nums1[i-1] > nums2[j]:
                imax = i-1
            else:
                if lenA == 0:
                    if (lenA + lenB) % 2 == 0:
                        return (nums2[int(lenB / 2)] + nums2[int(lenB / 2) - 1]) / 2
                    else:
                        return nums2[int(lenB / 2)]
                min_right,max_left = 0 , 0
                if i == 0:
                    max_left = nums2[j-1]
                elif j == 0:
                    max_left = nums1[i-1]
                else: 
                    max_left = max(nums1[i-1],nums2[j-1])
 
                if i == lenA:
                    min_right = nums2[j]
                elif j == lenB:
                    min_right = nums1[i]
                else:
                    min_right = min(nums1[i],nums2[j])
                if (lenA+lenB)%2 == 0:
                    return (max_left + min_right) / 2
                else:
                    return min_right