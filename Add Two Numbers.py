#You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first = []
        second = []
        while(l1!=None):
            first.append(l1.val)
            l1 = l1.next
        while(l2!=None):
            second.append(l2.val)
            l2 = l2.next
        total = str(int("".join(map(str, first[::-1]))) + int("".join(map(str, second[::-1]))))
        listOfNodes = []
        for i in total[::-1]:
            newNode = ListNode(i)
            listOfNodes.append(newNode)
        head = listOfNodes[0]
        for k in range(len(listOfNodes)-1):
            listOfNodes[k].next = listOfNodes[k+1]
        return head
