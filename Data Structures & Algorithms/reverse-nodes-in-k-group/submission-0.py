# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        
        i = 0
        final_lst = []
        while k <= len(lst):
            final_lst.extend(reversed(lst[0:k]))
            lst = lst[k:]
        if lst:
            final_lst.extend(lst)

        dummy = ListNode()
        current = dummy
        for i in final_lst:
            dummy.next = ListNode(i)
            dummy = dummy.next
        return current.next
