class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #First we create the dictionary:
        #The dictionary will act as out frequency counte
        freq_dict = dict()

        for num in nums:
            #We need an if/else block here to check if this number is not 
            #in the dictionary. If its not-> Assign a new key and add its initial counter of 1
            #If it already exists, we need to lookup the key and increment the counter
            if num in freq_dict:
                freq_dict[num] += 1

            else:
                freq_dict[num] = 1

        #Now we need to extract the top k elements
        #The frequencies in our dicts are the values
        #So we need to order the values such that we slice the top k values

        #Initially to sort this, we would've written: sorted(freq_dict.values())
        #However, we get a data loss issue. We lose the actual keys and just get the frequencies
        #as is.

        #So to solve this we use .items() to return a tuple. Since tuples are immutable, we can use
        #them as a key in the dictionary-> Format: (number, frequency)

        #Now we end up with a list of tuples we have to sort. How do we do this?->sorted() combined with 
        #custom lambda function

        sorted_items = sorted(freq_dict.items(), key = lambda x:x[1], reverse=True)

        
        #Now we need to do index slicing to get the k frequent elements:

        result = []
        #Index slice: [:k] where k is the stop index and we start at the beginning
        for item in sorted_items[:k]:
            #Remember, item is the tuple. E.g item = (1,3) where 1 = item[0] and 3 = item[1]
            #We always want the 'key (item[0]) since thats the information we need to output
            result.append(item[0])
        return result


            
