class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        #An anagram is a word that contains exact same CHARS as another word. Order 
        #doesn't have to be the same

        #First thing we need to check is if the length of each string is the same otherwise
        #it would not be a valid anagram

        if len(s) != len(t):
            return False

        else:

            #Create two dicts, one for s and one for t:
            
            s_count = {}
            t_count = {}

            #How are we going to loop through each string to 'get' the count of each char?
            #In python, we can simply use the get() method:

            for char in s:
                #Translation: The char we are looking at is retrieved and the count is being added
                s_count[char] = s_count.get(char, 0) + 1

            for char in t:
                t_count[char] = t_count.get(char, 0) + 1
            
        
        return s_count == t_count