from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Proposal
# 1. Keep a counter, current node and next node
# 2. When the counter reach the nth node, remove the
# reference from the current node to next node and replace
# it with current node to next next node
# note: the question require it to remove from the END of
# the linked list, we need to count the length of the
# linked list to understand the index from the front


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        length = 1 if head else 0
        node = head
        while node.next:
            length += 1
            node = node.next

        index = length - n - 1

        if index < 0:
            return head.next

        counter, current, next = 0, head, head.next

        while counter < index and\
                next is not None and\
                current is not None:
            current = next
            next = next.next if next else None
            counter += 1

        # skip a reference
        current.next = next.next if next else None

        return head


# Approach (two-pointer)
# 1. First iterate the right pointer to the nth position,
# from the left
# 2. Following that iterate the left position, until the
# right position reach the end
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left, right = dummy, head

        while n > 0 and right:
            n -= 1
            right=right.next

        while right:
            left = left.next
            right = right.next

        # now skip a reference
        left.next = left.next.next

        return dummy.next



def main():
    node2 = ListNode(2)
    node1 = ListNode(1, node2)
    head = Solution().removeNthFromEnd(node1, n=1)
    while head.next:
        print(head.val)
        head = head.next


if __name__ == "__main__":
    main()
