# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        unique_item = set()

        while head:
            if head in unique_item:
                return True
            else:
                unique_item.add(head)
            head = head.next
        return False