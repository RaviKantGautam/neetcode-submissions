# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lst = []
        head = ListNode()

        for lt in lists:
            current = lt
            while current:
                lst.append(current.val)
                current = current.next
        lst = sorted(lst)
        dummy = head
        for i in lst:
            dummy.next = ListNode(i)
            dummy = dummy.next
        return head.next