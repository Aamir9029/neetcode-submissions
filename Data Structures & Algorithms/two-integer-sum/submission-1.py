class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

       #Mental model:
       #Let current_index = j and past_index = i
       #We use j as the tracker in the array we are iterating over and i
       #is like a static number we pull from the dictionary 

       #We need both index AND value so we have to use a dictionary
       seen = {}

       #Python loop to keep track of both index and value
       #N.B: We need to keep track of two things which is the current_index(j) and the value 
       #at index j which is 'num'
       for j, num in enumerate(nums):

            #Equation
            #N.B -> Prev we wrote diff = target - nums[j]. Since we already used enumerate,
            #we already have the value at hand in 'num'
            diff = target - num

            #The difference will give us a hit or miss for the other matching number
            #If the diff is in the seen dict, we assign i as the index for that value
            #else we simply just add it to the dict for future use
            if diff in seen:

                i = seen[diff]

                return [i,j]
            #This else block is important since this will take a 'snapshot' of the current state
            #and store it in the dict. When the loop goes back to the top, j is now a different value
            #but it stored its previous value in the iteration before so we have a record in the seen dict    
            else:
                seen[num] = j
                

