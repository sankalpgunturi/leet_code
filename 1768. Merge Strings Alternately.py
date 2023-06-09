class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        final = ''
        l, r = 0, 0
        while l < len(word1) or r < len(word2):
            if l < len(word1):
                final += word1[l]
            if r < len(word2):
                final += word2[r]
            l += 1
            r += 1
        
        return final
      
