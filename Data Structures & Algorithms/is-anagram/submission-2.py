class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #EDGE CASE: Before we can even do any logic, a valid
        #anagram will require both strings to have the same amount 
        #of letters:
        if len(s) != len(t):
            return False

        else :

            #Dictionaries to track count of chars in each string
            countS = {}
            countT = {}
            
            for char in s:
                countS[char] = countS.get(char, 0) + 1

            for char in t:
                countT[char] = countT.get(char, 0) + 1

            #Now we have the count dictionaries updated with counts for each char in 
            # s and t

            return countS == countT

        return False