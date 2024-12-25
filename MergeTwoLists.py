from typing import Optional
import math
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Merge two sorted lists
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None:
            return None
        result = ListNode()
        result_root = result
        result_pointer = result

        list1_pointer = list1
        list2_pointer = list2
        while list1_pointer != None or list2_pointer != None:
            val1 = math.inf
            if list1_pointer != None:
                val1 = list1_pointer.val

            val2 = math.inf
            if list2_pointer != None:
                val2 = list2_pointer.val

            if val1 <= val2:
                result_pointer.val = list1_pointer.val
                list1_pointer = list1_pointer.next
                if list1_pointer != None or list2_pointer != None:
                    result_pointer.next = ListNode()
                    result_pointer = result_pointer.next
            else:
                result_pointer.val = list2_pointer.val
                list2_pointer = list2_pointer.next
                if list2_pointer != None or list1_pointer != None:
                    result_pointer.next = ListNode()
                    result_pointer = result_pointer.next

        return result_root


            