class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        
        for index,val in enumerate(nums):
            difference = target - val
            
            if difference in prevMap:
                return [prevMap[difference],index]
            prevMap[val] = index
