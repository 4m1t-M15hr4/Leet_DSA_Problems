# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode | None) -> int:
        binary = 0
        temp = head
        while temp is not None:
            binary = binary * 2 + temp.val
            temp = temp.next
        return binary

        