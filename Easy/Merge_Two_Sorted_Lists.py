# -*- coding: utf-8 -*-
"""
Merge Two Sorted Lists
Easy

Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

Input: l1 = [], l2 = []
Output: []

Input: l1 = [], l2 = [0]
Output: [0]

將l1和l2的節點由小到大排序組合。

解題要點
1.用iterative(迭代或迴圈)比較好想，當然也有recursive(遞迴)的方式來解
2.上述方式時間複雜度worst case是O(N1+N2)，best case是O(min(N1, N2))

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dum = ListNode(None) # 使dummy node 一直保持同樣的位置，並指向第一個節點
        prev = dum #用來指定比較過後較小的節點，並用next來取得
        
        while l1 and l2:
            if l1.val <= l2.val:  #判斷誰小，小的就讓prev.next並準備接下一節點，小的本身也要next到下一節點
                prev.next = l1 
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
            
        if l1 == None:      #當其中一個陣列用光後，將剩餘的陣列節點排序下去
            prev.next = l2
        elif l2 == None:
            prev.next = l1
        
        return dum.next  #輸出dum ，因為dum始終沒被動過，其他節點都被改動過位址了