# class Solution:
#     def addtwonumbers(self, nums1, nums2):
#         nums1.reverse()
#         nums2.reverse()

#         number1 = 0
#         for digit1 in nums1:
#             number1 = number1 * 10 + digit1

#         number2 = 0
#         for digit2 in nums2:
#             number2 = number2 * 10 + digit2

#         result = number1 + number2

#         return [int(d) for d in str(result)][::-1]
    
# sol = Solution()
# l1 = [2, 4, 3]  
# l2 = [5, 6, 4]  
# print(sol.addtwonumbers(l1, l2))  




class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Initialize a dummy node to simplify the addition process
        dummy = ListNode()
        current = dummy
        carry = 0
        
        # Traverse both linked lists
        while l1 or l2 or carry:
            # Get the values of the current nodes (or 0 if the list is exhausted)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the sum and the carry
            total = val1 + val2 + carry
            carry = total // 10
            total = total % 10
            
            # Create a new node with the sum and attach it to the result list
            current.next = ListNode(total)
            current = current.next
            
            # Move to the next nodes in the lists
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        # The next node of dummy is the head of the resulting linked list
        return dummy.next

# Helper function to create a linked list from a list of integers
def create_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for number in lst:
        current.next = ListNode(number)
        current = current.next
    return dummy.next

# Helper function to print a linked list
def print_linked_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# Test cases
solution = Solution()

l1 = create_linked_list([2, 4, 3])
l2 = create_linked_list([5, 6, 4])
result = solution.addTwoNumbers(l1, l2)
print_linked_list(result)  # Output: 7 -> 0 -> 8 -> None

l1 = create_linked_list([0])
l2 = create_linked_list([0])
result = solution.addTwoNumbers(l1, l2)
print_linked_list(result)  # Output: 0 -> None

l1 = create_linked_list([9, 9, 9, 9, 9, 9, 9])
l2 = create_linked_list([9, 9, 9, 9])
result = solution.addTwoNumbers(l1, l2)
print_linked_list(result)  # Output: 8 -> 9 -> 9 -> 9 -> 0 -> 0 -> 0 -> 1 -> None
