class Solution:

    def encode(self, strs: List[str]) -> str:

        #Need to store encoded string in a var
        encoded_string = ""
        #Loop through the array
        for s in strs:
            length = len(s)
            #Add the length of each string with a '#' and then the actual string
            #Concept = Length prefix encoding
            encoded_string += str(length) + "#" + s
        
        return encoded_string


    def decode(self, s: str) -> List[str]:
        
        #Need to loop through the given encoded string(param = s-> this is what we iterate on)
        #We need to first initialize:

        result = [] #Variable to hold the decoded strings
        i = 0   #Main pointer variable

        #Right now, i is sitting at the start of the encoded string. We need to somehow recognize
        #the digit that has been prepended and then stop at the '#' character.

        #We need to iterate over two indices here in a while loop (i and j). Index i will be for
        #the word chunk and the index j will be for the digit tracking and # delimiters


        while i < len(s):
            j = i #Both start at same place at beginning of encoded string
            #Pointer j goes to work here by finding the '#'
            while s[j] != "#":
                j += 1 # Keep incrementing j

            #Extract length number(for word jumps)
            #The digit we prepended in the decoding needs to be found here and since its a 
            #string, we typecast with an int to get the actual numeric value to do math with later

            length = int(s[i:j])

            #Now we extract the actual word and add to results array:
            #1) Word starts at j + 1
            #2) Word ends at (j + 1) + length
            word = s[j + 1: j + 1 + length]
            result.append(word)

            #This is for our i pointer to go to the next iteration to extract the next word
            i = j + 1 + length
            
        return result            
         
