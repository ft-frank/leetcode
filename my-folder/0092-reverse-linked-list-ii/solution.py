# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Traverse the linked list until we reach the left position. Seems like it is 1-indexed.
Then start the linked list reversal (signature 4-step method), until we reach right position. 
Then reattach the new start of the linked list to left, and new end of linked list to right.


"""
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        #i need dummy node strategy
        dummy = ListNode()
        dummy.next = head
        i = 1
        cur = head
        prev = dummy
        while i < left:
            prev = cur
            cur = cur.next
            i += 1
        start = prev
        end_list = cur
        prev = None
        #now i == left, and cur is on the current, and start is the node we have to reattach

        #reversal
        while i <= right:
            temp = cur.next #save next node
            cur.next = prev #the current node's next node is the previous node (reverse)
            prev = cur #save previous node
            cur = temp #momve the current node to the next node
            i += 1
        #now temp should be the node to the right of the right node, and cur 
        end = temp
        front_list = prev
        #now we need to reattach

        start.next = front_list
        end_list.next = end

        return dummy.next

"""
Returning head is not accurate, because the head could be moved
A linked list with two nodes are unable to switch around

"""





        
        
            

