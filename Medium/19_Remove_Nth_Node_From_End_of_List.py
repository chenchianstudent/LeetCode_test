# -*- coding: utf-8 -*-
"""
Remove Nth Node From End of List
Medium

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Input: head = [1], n = 1
Output: []

Input: head = [1,2], n = 1
Output: [1]


給你 n，叫你把陣列倒數n的位置數字刪除並輸出刪除後的陣列。

解題思路
這題直接想到快慢指針，先讓快的去跑陣列，再讓慢的間隔 n後出發。
這樣當快指針跑完後，慢指針就會停在要刪除的位置上。
而因為要刪除慢指針的位置，我們會需要另一個點去記錄前面那個節點的位置

由於可能刪除首節點，我們會使用啞節點當作的新的起點。

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        root = ListNode(0 , head)
        fast,slow,pre = root,root,root # 快指針、慢指針、紀錄刪除位置的前一點
        
        while n-1:
            fast = fast.next
            n -= 1
        while fast.next: #當快指針下一節點還有值的時候
            fast = fast.next
            pre = slow
            slow = slow.next
        pre.next = slow.next
        return root.next