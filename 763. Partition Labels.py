class Solution:
    def partitionLabels(self, s):
        last = {val: index for index, val in enumerate(s)}
        res = []
        maxindex = -1
        cnt = 1

        for index, val in enumerate(s):
            maxindex = max(maxindex, last[val])
            if maxindex == index:
                res.append(cnt)
                cnt = 1
            else:
                cnt += 1
        return res

a = Solution()
s = ["ababcbacadefegdehijhklij", "eccbbbbdec"]
for c in s:
    print(a.partitionLabels(c))
