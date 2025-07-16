class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        #loop through the range of the length of the array
        for i in range(len(nums)):
            #finds if the y value we want exists since target and nums[i] are values we have
            checkHash = target - nums[i]
            #checks if y value is in hashmap so we dont need to loop anymore (cuts down time)
            if (checkHash in hashmap):
                #returns correct position of values we know equal the target when added
                return [i,hashmap[checkHash]]
            #set new hashmap key/value pair
            hashmap[nums[i]] = i
        #return empty array
        return []       

