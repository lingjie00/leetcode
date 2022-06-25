from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __str__(self):
        return str(self.val)

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # iterative approach
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        prev = None
        cur = head

        while cur:
            # print("start", prev, cur, next)

            tmp = prev

            prev = cur
            cur = cur.next

            prev.next = tmp

            # print("end", prev, cur, next)

        return prev


class Solution:
    # recursive approach
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def reverse(prev, cur):
            print(prev, cur)

            if cur is None:
                return prev

            tmp = cur.next
            cur.next = prev

            return reverse(cur, tmp)

        node = reverse(None, head)

        return node


if __name__ == "__main__":
    head = [1, 2, 3, 4, 5]
    nodes = []
    currNode = ListNode(head[0])
    for i in range(1, len(head)):
        nodes.append(currNode)
        nextNode = ListNode(head[i])
        currNode.next = nextNode
        currNode = nextNode

    endNode = Solution().reverseList(nodes[0])

    while endNode:
        print(endNode.val)
        endNode = endNode.next if endNode else None
