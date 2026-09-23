# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        while head is not None and head.val == val:
            head = head.next
            
        temp = head
        while temp is not None and temp.next is not None:
            if temp.next.val == val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return head
