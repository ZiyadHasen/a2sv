class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==1:
            return [[1]]

        prev= self.generate(numRows-1)  
        temp=[1]
        for i in range(len(prev[-1])-1):
            temp.append(prev[-1][i]+prev[-1][i+1]) 
        temp.append(1)    
        # print(temp)    
        prev.append(temp)
        return prev


       
        