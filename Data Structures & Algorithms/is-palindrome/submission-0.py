class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        #Two pointer concept: L and R pointer that converge in middle

        left = 0
        right = len(s) - 1

        #Standard loop for two pointer convergence:

        #To avoid overlapping
        #Outer main loop:

        #EDGE CASE: s = "    ". So left = 0, right = 3. We will get an overlap if
        #we dont have the same 'left<right condition in the inner while loop

        while left < right:

            while left < right and (not s[left].isalnum()):
                left += 1
            
            
            while left < right and (not s[right].isalnum()):
                right -= 1

            #Now we need to compare the chars but need to convert to lowercase in place:

            if s[left].lower() != s[right].lower():
                return False

            else:
                #If they match, keep converging
                left += 1
                right -= 1

        return True




