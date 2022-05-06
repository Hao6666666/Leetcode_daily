class Solution:
    def removeDuplicates(self, s, k) -> str:

        stack = []  ## [character, count]

        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
            else:
                stack.append([c, 1])
            while stack and stack[-1][1] == k:
                stack.pop()
        return ''.join([c * n for c, n in stack])
a = Solution()
s = "deeedbbcccbdaa"
k = 3
print(a.removeDuplicates(s, k))