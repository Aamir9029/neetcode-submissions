class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_set = set()

        for num in nums:
            #Check first if the number is already there
            if num in my_set:
                return True
            #If not, add it to the set
            my_set.add(num)
        
        #Loop finishes and no duplicates:
        return False

            