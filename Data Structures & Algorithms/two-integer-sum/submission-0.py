class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dt = {}
        index = []
        for i in range(len(nums)):
            dt[nums[i]] = target - nums[i]
            if dt[nums[i]] in nums:
                index =  [nums.index(dt[nums[i]]), i]
        return index

                

        
        