class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr=[0]*26
        
        size=len(s)
        for i in range(size):
         index=ord(s[i])-ord('a')

         arr[index]+=1
         if arr[index]==2:
           return s[i]
    
        return ""
