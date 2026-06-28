class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        #Need to have a set to keep track of what is currently in our window to avoid repeats:
        char_set = set()

        left = 0 #init the left pointer only
        longest_streak = 0 #keep track of longest substring as per problem statement

        #Now we need to loop through the string with our right pointer

        for right in range(len(s)):
            #Shrink phase: If the new char breaks the rule, shrink from the left of the window
            #Rule breaks if the right pointer is already in the set
            while s[right] in char_set:
                #Need to delete the repeated character which is 
                #N.B: A substring is a CONTIGUOUS sequence of chars within a string
                #We need to remove the left pointer from the set and increment it
                char_set.remove(s[left])
                left += 1

            #Expand phase: The window is valid, Add the new char
            char_set.add(s[right])

            #Tracking: The biggest window we have seen so far:
            #Why right - left + 1? If we are at the beginning, both l and r are at 0
            #There is only 1 char inside the window. Therefore 0 - 0  = 0 but this is wrong since
            #our window is size 1. THat is why we have the +1 (universal rule in programming)
            longest_streak = max(longest_streak, right - left + 1)    
        
        return longest_streak
