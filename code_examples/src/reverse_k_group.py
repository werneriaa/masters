# # https://leetcode.com/problems/reverse-nodes-in-k-group/
# # Grade: Hard
# # Solution: https://leetcode.com/problems/reverse-nodes-in-k-group/solutions/4675368/simple-and-easy-commented-code-iterative-approach/


# def reverseKGroup(head, k):
#     # Check if there are at least k nodes
#     count = 0
#     curr = head
#     while curr and count < k:
#         curr = curr.next
#         count += 1
#     if count < k:
#         return head

#     # Reverse the current group
#     prev = None
#     curr = head
#     for _ in range(k):
#         next_node = curr.next
#         curr.next = prev
#         prev = curr
#         curr = next_node

#     # Recursively reverse the remaining groups
#     head.next = reverseKGroup(curr, k)

#     return prev
