class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if(nums[j] == target - nums[i]):
                    return ([i,j])
        return []       


        
"double for loop is needed for brute force approach"
"hashmap needed for better complexity"