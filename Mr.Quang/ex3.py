class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def add_two_numbers(l1, l2):
    dummy = ListNode(0)  # Dummy node to track the head of the result list
    current = dummy  # Pointer to traverse the result list
    carry = 0  # Carry value for addition

    while l1 or l2 or carry:
        # Extract the values from the linked lists
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        # Perform addition and update the carry
        total = val1 + val2 + carry
        carry = total // 10
        digit = total % 10

        # Create a new node with the calculated digit and append it to the result list
        current.next = ListNode(digit)
        current = current.next

        # Move to the next nodes in the linked lists if they exist
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next  # Return the head of the resulting linked list
# Create the first linked list: 2 -> 4 -> 3 (represents the number 342)
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

# Create the second linked list: 5 -> 6 -> 4 (represents the number 465)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

# Add the two numbers
result = add_two_numbers(l1, l2)

# Print the result
while result:
    print(result.val, end=" ")
    result = result.next

# Output: 7 0 8 (represents the number 807)
