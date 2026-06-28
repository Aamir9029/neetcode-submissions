class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        #Two pointer technique:

        left = 0
        right = len(numbers) - 1

        #So we dont have overlapping and we dont use the same element twice
        #How does this enforce we dont use the same element twice?:
        #Case: [2,5,8], target = 10
        #If we wrote left <= right, eventually l and r pointers will land on 5.
        #We are not allowed to have i = j. (l = r). So the < saves us
        while left < right:

            #Need to calculate the current_sum of numbers at left and right pointers
            #First we need safety checks:

            #Remember: what we need to return is 1-indexed
            current_sum = numbers[left] + numbers[right]

        
            #1. What if current_sum == target? -> return the l and r pointers 
            #   but add 1 to them to comply with the 1-indexed rule
            if current_sum == target:
                return [left + 1, right + 1]

            #2. What if current_sum is greater than the target?
            #   Since the array is already SORTED, which pointer do we move
            #   to make the sum smaller? -> The right pointer.

            elif current_sum > target:
                right -= 1

            #3. What if current_sum is less than target?
            #   Which pointer to move? -> left(since also array is sorted)-> We do this 
            #   to make the summ bigger
            else :
                left += 1

        return [left, right]        



            