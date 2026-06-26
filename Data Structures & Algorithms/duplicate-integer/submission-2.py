class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        #We need to add all the elements one by one into a SET
        #and need a conditional to check if the number already exists in this set:

        #Initialize the set
        my_set = set()

        for num in nums:
            #Check if the num is already in the set:
            if num in my_set:
                return True
            else:
                my_set.add(num)
        return False
            