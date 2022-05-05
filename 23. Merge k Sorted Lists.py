# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        heap = []
        heapq.heapify(heap)

        for index, l in enumerate(lists):
            if l:
                heapq.heappush(heap, (l.val, index))  ## push 进去所有list的head的val, 即第一位元素

        dummy = ListNode(0)
        cur = dummy
        while heap:
            val, index = heapq.heappop(heap)
            cur.next = ListNode(val)  # 因为pop出来的是int，所以可以直接放进ListNode
            cur = cur.next  # 一定记得cur = cur.next

            if lists[index].next:  # 一定是先把前三个head比较完，才会开始比较后面push进去的val，所以在每一个head.next存在的时候可以放心把后面的元素插入进heap, heap自动排序
                heapq.heappush(heap, (lists[index].next.val, index))
                lists[index] = lists[index].next
        return dummy.next
