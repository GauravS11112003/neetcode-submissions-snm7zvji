class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        sorted_nums = sorted(nums)
        n = len(sorted_nums)
        
        res = []

        for i in range(len(sorted_nums)):
            
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue
            
            left = i + 1
            right = n - 1

            while left < right:

                sum = sorted_nums[i] + sorted_nums[left] + sorted_nums[right]

                if sum == 0:
                    res.append([sorted_nums[i], sorted_nums[left], sorted_nums[right]])
                    left += 1
                    
                    while left < right and sorted_nums[left] == sorted_nums[left - 1]:
                        left += 1

                elif sum > 0:
                    right -= 1

                elif sum < 0:
                    left += 1

        return res