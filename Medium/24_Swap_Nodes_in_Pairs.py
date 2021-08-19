# -*- coding: utf-8 -*-
"""
Swap Nodes in Pairs
Medium

Input: head = [1,2,3,4]
Output: [2,1,4,3]

Input: head = []
Output: []

Input: head = [1]
Output: [1]

給你一個鏈表，交換相鄰的節點，並返回鏈表的起點。

這裡要注意！！！不能修改鏈表的值，只能修改節點。空間複雜度僅能O(1)

"""
'''解法一，每次相鄰的節點進行交換，我們就將兩個節點當一個單位做處理，循環每次交換兩個節點。'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: #先排出特殊情況
            return head
        pre = new_head = ListNode(0) #建立移動指標pre和不移動的new_head
        while head and head.next:
            tmp = head.next       #類似氣泡排序法的交換，會有一個tmp當暫存器
            head.next = tmp.next  
            tmp.next = head
            pre.next = tmp
            pre = head
            head = head.next
        return new_head.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''解法二(較佳解)，解法一的延伸。反正都是要創造新的ListNode去把兩個節點加進來，何不每次添加兩節點時將原表上的相鄰節點以逆序加進'''
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: #先排出特殊情況
            return head
        new_head = head.next
        head.next = self.swapPairs(head.next.next)
        new_head.next = head
        return new_head