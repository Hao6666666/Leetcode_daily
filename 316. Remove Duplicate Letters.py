class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last = {val: index for index, val in enumerate(s)}
        seen = set()
        stack = []

        for i in range(len(s)):
            if s[i] in seen:
                continue
            while stack and s[i] < stack[-1] and last[stack[-1]] > i:
                seen.remove(stack[-1])
                stack.pop()

            stack.append(s[i])
            seen.add(s[i])
        return ''.join(stack)

a = Solution()
s = "cbacdcbc"
print(a.removeDuplicateLetters(s))