class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            checkHash = target - nums[i]
            if (checkHash in hashmap):
                return [i,hashmap[checkHash]]
            hashmap[nums[i]] = i
        return []       

