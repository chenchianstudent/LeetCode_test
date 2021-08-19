# -*- coding: utf-8 -*-
"""
Merge k Sorted Lists
Hard

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Input: lists = []
Output: []

Input: lists = [[]]
Output: []


給你list，讓你從小到大排列。
這題如果沒有時間限制的話還蠻簡單的，用指標慢慢推最小值然後放進新的陣列中再輸出就好，但時間複雜度偏長，會time out。

這題我自認能力不足，去爬了好幾個文章，看起來比較好的解法就是用heapq --- 堆積佇列 (heap queue) 演算法

堆積佇列 (heap queue) 演算法
Heap（堆積）是一顆二元樹，樹上所有父節點的值都小於等於他的子節點的值。
使用陣列實作，對於所有從0開始的 k 都滿足 heap[k] <= heap[2*k+1] 和 heap[k] <= heap[2*k+2] 。
為了比較節點的值，不存在的元素被視為無限大。heap 存在一個有趣的性質：樹上最小的元素永遠會在根節點 heap[0] 上。

參考影片:
https://www.youtube.com/watch?v=YC7jKAr8FJ0&ab_channel=%E4%BB%8A%E5%A4%A9%E6%AF%94%E6%98%A8%E5%A4%A9%E5%8E%B2%E5%AE%B3
https://www.youtube.com/watch?v=ptYUCjfNhJY&ab_channel=BackToBackSWE

最後我是採用後者的方式去做
runtime就變成了Runtime: 92 ms, faster than 93.64% of Python3 online submissions for Merge k Sorted Lists.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = [] # 建立heap陣列
        
        for i in lists:
            while i:
                heappush(min_heap, i.val) #heapq.heappush(heap, item) >>>把 item 放進 heap，並保持 heap 性質不變。
                i = i.next
        
        dummy = head = ListNode(-1)
        
        while min_heap:
            head.next = ListNode(heappop(min_heap)) 
            #heapq.heappop(heap) 從 heap 取出並回傳最小的元素，同時保持 heap 性質不變。
            #如果 heap 是空的會產生 IndexError 錯誤。只存取最小元素但不取出可以使用 heap[0] 。
            head = head.next
            
        return dummy.next