class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i=0
        r=len(height)-1
        area=0
        
        while(i<r):
            area = max(area, min(height[i],height[r])*(r-i))
          
            if(height[i]<height[r]):
                i+=1
            else:
                r-=1
                
        return(area)
                
            


                    
        
