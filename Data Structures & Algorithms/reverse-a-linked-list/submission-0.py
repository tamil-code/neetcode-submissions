# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        next_node = head
        while next_node!=None:
            temp = next_node.next
            next_node.next = prev
            prev = next_node
            next_node = temp
        return prev
        