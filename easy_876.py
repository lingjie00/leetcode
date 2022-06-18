# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Proposal:
# 1. Find out the total length of the linked list
# 2. Iterate through the list again to extract the middle node
# time: O(n)
# space: O(1)

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # find the total length
        counter = 0
        next = head
        while next.next is not None:
            next = next.next if next else None
            counter += 1

        # get the middle node counter
        mid = counter // 2
        if counter % 2:
            # take the second middle node
            mid += 1

        # find the second middle node
        next = head
        counter = 0
        while counter < mid:
            next = next.next if next else None
            counter += 1

        return next

# Approach
# 1. Implement fast and slow pointer
# 2. Fast pointer travels two nodes while slow pointer
# travel one node
# 3. At the end, when the fast pointer complete the linked
# list, the slow pointer will be at the middle
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow
