# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #dummy node is used for referencing the head of the linkedList as thats prone to changing
        mergedList = dum = ListNode()
        #double while for looping through both lists
        while list1 and list2:
            #since the lists are in increasing order we can check for which one to add 
            #to the merged list
            if list1.val < list2.val:
                mergedList.next = list1
                list1, mergedList = list1.next, list1
            else:
                mergedList.next = list2
                list2, mergedList = list2.next, list2

        #checks for empty list
        if list1 or list2:
            mergedList.next = list1 if list1 else list2
        return dum.next
        