# -*- coding: utf-8 -*-
"""
Add Two Numbers
Medium

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
"""
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0  #紀錄進位數字
        dummy = ListNode()
        curr = dummy
        while l1 != None or l2 !=None: # 當l1 和 l2的長度都還有的時候就繼續做
            if l1 != None:
                carry +=l1.val
                l1 = l1.next
            if l2 != None:
                carry +=l2.val
                l2 = l2.next 
            curr.next = ListNode(carry % 10) # carry/10的餘數當作新ListNode的輸出
            if carry>=10: # 確認carry是否要進位
                carry = 1
            else:
                carry = 0
            curr = curr.next
        if carry !=0: # 確認當l1與l2 next到最後一項後，carry剩餘的進位數是否需要加進新的ListNode中  
            curr.next = ListNode(carry)
        return dummy.next