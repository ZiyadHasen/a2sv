class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res=[]
        s=list(words[0])
        count_shared= Counter(s)        

        
        for word in words[1:]:
            
             count_shared =count_shared & Counter(word)
        result = list(count_shared.elements())
        return result


