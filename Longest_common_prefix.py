#Write a function to find the longest common prefix string amongst an array of strings.

#If there is no common prefix, return an empty string "".

#Example 1:

#Input: ["flower","flow","flight"]
#Output: "fl"
#Example 2:

#Input: ["dog","racecar","car"]
#Output: ""
#Explanation: There is no common prefix among the input strings.



class Solution:

        
        
        
        
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        if(not strs):
            return ""
        shortest = min(strs, key = len)
        print(shortest)
        
       # x="flight"
        str_to_return=""
        
        for i in range(len(shortest)):
            if(all([x.startswith(shortest[:i+1]) for x in strs])):
                str_to_return = shortest[:i+1]
            else:
                break
                
        return(str_to_return)
                
            
        
