class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]] = 1
            else:
                freq[nums[i]] += 1

        arr = list(freq.keys())

        count = [[] for _ in range(len(nums) + 1)]

        for a in range(len(arr)):
            if arr[a] not in count:
                count[freq[arr[a]]].append(arr[a])

        final = []

        for c in range(len(count)-1, 0, -1):
            for n in count[c]:
                final.append(n)
            if len(final) == k:
                return final

