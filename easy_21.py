from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self,
                      list1: Optional[ListNode],
                      list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()

        node = dummy

        while list1 or list2:

            if not list1:
                node.next = list2
                break
            elif not list2:
                node.next = list1
                break

            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next if list1 else None
            else:
                node.next = list2
                list2 = list2.next if list2 else None

            node = node.next

        return dummy.next
