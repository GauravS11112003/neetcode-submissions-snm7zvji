class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dt = {}
        index = []
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in dt:
                index = [dt[difference], i]
            else:
                dt[nums[i]] = i
        return index

        
        