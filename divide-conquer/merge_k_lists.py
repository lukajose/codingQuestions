from typing import List


class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next


class Solution:
    # given two sorted lists merge them into one
    def merge(self,l1:ListNode,l2:ListNode) -> ListNode:
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        m = ListNode(0)
        if l1.val > l2.val:
            m.val = l1.val
            l1 = l1.next
        else:
            m.val = l2.val
            l2 = l2.next
        
        
        while l1.next != None and l2.next != None:
            le = l1.val
            se = l2.val
            if le > se:
                m.next = ListNode(se)
                l1 = l1.next
            elif le <= se:
                m.next = ListNode(le)
                l2 = l2.next
        # merge remaining l1
        while l1 !=  None:
            m.next = ListNode(l1.val)
            l1 = l1.next
        # merge remaining l2
        while l2 != None:
            m.next = ListNode(l2.val)
            l2 = l2.next

        return m
        


    
    def merge_k_lists(self,lists) -> ListNode:
        k = len(lists) - 1
        while k != 0:
            i = 0
            j = k
            while(i < j):
                lists[i] = self.merge(lists[i],lists[j])
                i+=1
                j-=1
            if i >= j:
                k = j
        return lists[0]
def main():
    k = 3
    lists = [0 for i in range(k)]
    lists[0] = ListNode(1)
    lists[0].next = ListNode(3)
    lists[0].next.next = ListNode(5)

    lists[1] = ListNode(1)
    lists[1].next = ListNode(4)
    lists[1].next.next = ListNode(6)
    
    lists[2] = ListNode(2)
    lists[2].next = ListNode(2)
    lists[2].next.next = ListNode(20)

    sol = Solution()
    m = sol.merge_k_lists(lists)

    while m != None:
        print(f"[{m.val}] -> ",end=" ")
        m = m.next
    print("NULL")



main()