from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        result: ListNode = None
        values = []

        for node in lists:
            values = self.__createSliceFromListNode(node, values)

        values.sort(reverse=True)
        for value in values:
            result = ListNode(value, result)

        return result
    
    def __createSliceFromListNode(self, listNode: Optional[ListNode], values: list) -> list:
        while listNode != None:
            values.append(listNode.val)
            listNode = listNode.next
        
        return values