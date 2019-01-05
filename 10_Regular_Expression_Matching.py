class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        table =  [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        
        
        table[0][0]=True
        #print(table)
        
        numrows = len(table)    # 3 rows in your example
        numcols = len(table[0]) 
        #print(numrows,numcols)
        #row,col=table.size()
        #print(row,col)
        for t in range(1,numcols):
            if(p[t-1]=='*'):
                table[0][t] = table[0][t-2]
        for i in range(1,numrows):
            for j in range(1,numcols):
         #       print(i,j)
                
                if ((s[i-1]==p[j-1]) or (p[j-1]=='.')):
                    table[i][j]=table[i-1][j-1]
          #          print(table)
           #         print("hello")
                    # if ((i==1) and (j==1)):
                    #     x=table[i-1][j-1]
                        

                elif (p[j-1]=='*'):
                    table[i][j]=table[i][j-2]
                    if(p[j-2]=='.' or s[i-1]==p[j-2]  ):
            #            print("jj",table[i-1][j],i,j)
                        table[i][j]=table[i][j] or table[i-1][j]
             #           print(table)
                        
                    # else:
                    #     print("twoq")
                    #     table[i][j]=table[i][j-2]
                    #     print(table)
                        


                else:
                    print("three")
                    table[i][j]=False
                            
                        
        #print(table)
        return table[numrows-1][numcols-1]
        
