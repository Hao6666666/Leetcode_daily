class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ##slow走的只是nums[slow]的值，只走了一次。而fast，先走了nums[fast]，得到一个value值，算第一步，又走了nums[nums[fast]]，也就是nums[value]，这是第二步。所以每执行一次语句，fast走了两步，slow只走了一步，并不一定是按顺序走下来。
        ## 和142相似
        ## 142 题中慢指针走一步 slow = slow.next ==> 本题 slow = nums[slow]
        ## 142 题中快指针走两步 fast = fast.next.next ==> 本题 fast = nums[nums[fast]]

        slow = nums[0]
        fast = nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow





