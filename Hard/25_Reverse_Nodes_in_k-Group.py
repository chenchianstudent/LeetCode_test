# -*- coding: utf-8 -*-
"""
Reverse Nodes in k-Group
Hard

Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]

Input: head = [1,2,3,4,5], k = 1
Output: [1,2,3,4,5]

Input: head = [1], k = 1
Output: [1]

解題思路
利用分組的形式，將數字一組一組分好，當前的分組達到 k個節點後，就進行反轉。反之保持原樣。
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head, k):
            p = head
            for i in range(k): # #確認長度是否小於k，若小於就不反轉
                if p:
                    p = p.next
                else:
                    return head

            pre, now = head, head.next
            pre.next = None
            i = 1
            while(now != None and i < k): # 進行互換的動作
                nex = now.next
                now.next = pre
                pre, now = now, nex
                i += 1

            if now:
                head.next = reverse(now, k)

            return pre

        if head:
            return reverse(head, k)
        else:
            return None