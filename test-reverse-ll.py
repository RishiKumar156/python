class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

    def reverse_between_indices(self, left, right):
        if left == right:
            return

        dummy = ListNode(0)
        dummy.next = self.head
        prev = dummy

        # Move 'prev' to the node before the left index.
        for _ in range(left - 1):
            prev = prev.next
        while prev:
            print(prev.value)
            prev = prev.next 

        current = prev.next
        for _ in range(right - left):
            next_node = current.next
            current.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node

        # self.head = dummy.next

# Example usage
my_list = LinkedList()
for val in [1, 2, 3, 4, 5]:
    my_list.append(val)

print("Original List:")
my_list.print_list()

left_index = 2
right_index = 4
my_list.reverse_between_indices(left_index, right_index)

print("\nList after reversing from index", left_index, "to", right_index)
my_list.print_list()
