class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        num_set = set(nums)
        longest_streak = 0 #global var in function scope

        for num in nums:
            #if number before current num doesnt exist(num-1), this is the start of the sequence
            #Even if we have a test case like: [9,2,3,4,5], num - 1 = 8. 8 doesnt exist so
            #logic will flag 9 as the start of the sequence BUT this is still valid since the 
            #sequence will just be of length one. This is where a variable like "longest_streak"
            #will need to come in that tracks the max that we have seen so far.

            #If we go through the loop, we see that 10 doesnt exist so the streak will end
            #and so far the longest_streak var will be set to 1. Now we are at 2, we see that n-1
            #which is 1 doesnt exist so our if statement will trigger here and now we are at the start
            #of a new sequence. We start looking for 3, then 4, then 5. They all exist so now 
            #longest streak will be updated to 4. 

            if (num - 1) not in num_set:
                #We found the start of the sequence
                #Now we need to look for n+1
                #Implement while loop:

                #We need variables to track our progress:
                current_num = num
                current_streak = 1 #Everytime our if statement is triggered, this will be reset to 1

                #WHILE LOOP: How can we build on the current_streak?
                while (current_num + 1) in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak

