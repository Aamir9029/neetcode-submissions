class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #We use the dictionary bucket method here to group the strs
        
        #First we need to create the dictionary:
        anagram_dict = dict()

        for word in strs:
            #Generate key:
            sorted_word = "".join(sorted(word))

            #Normally you would check if the key already exists but we can 
            #reduce the code by not writing and if else after by using 'not in'
            if sorted_word not in anagram_dict:

                #We need to create the 'bucket' in our dictionary if this is 
                #a new key:
                anagram_dict[sorted_word] = []
            
            #------We dont have an else block if we used an 'if not in' statement. 
            #------There is no either or logic here.

            #Now we insert the word into this newly created bucket:
            #N.B-> To insert into a dictionary we APPEND
            anagram_dict[sorted_word].append(word)
        
        #The sorting logic is now finished, we just need to return the lists
        #We dont need the keys, just the values so we use .values(). 
        #BUT, the problem statement requires us to return sublists. So we need to 
        #wrap the command in a list() function
        return list(anagram_dict.values())



