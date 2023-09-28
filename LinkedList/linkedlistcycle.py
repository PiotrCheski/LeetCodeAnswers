class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        prevValues = set()
        curr = head
        while curr:
            if curr in prevValues:
                return True
            else:
                prevValues.add(curr)
                curr = curr.next
        return False