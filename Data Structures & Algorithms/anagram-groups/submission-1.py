class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dt = {}
        for s in range(len(strs)):
            count = [0] * 26
            for c in range(len(strs[s])):
                count[ord(strs[s][c])-ord('a')] += 1
            if tuple(count) not in dt:
                dt[tuple(count)] = [strs[s]]
            elif tuple(count) in dt:
                dt[tuple(count)].append(strs[s])
        return list(dt.values())