class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head) :
        seen = {}
        dummy = ListNode(0)  # Create a dummy node to handle the edge case of deleting the head
        dummy.next = head
        temp = dummy  # Start from the dummy node

        while temp.next:
            if temp.next.val in seen:
                temp.next = temp.next.next  # Skip the duplicate node
            else:
                temp = temp.next  # Move to the next node
                seen[temp.val] = True
        return dummy.next  # Return the modified linked list starting from the dummy's next
