class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        arr=[0]*26

        for i in range(0,len(s)):
            index = ord(s[i])-ord('a')
            arr[index]+=1
        
        for j in range(len(t)):
            index = ord(t[j]) - ord('a')
            arr[index] -= 1

        
        for i in range(26):
            if arr[i]== -1:
              return chr(ord('a') + i)
        
        return ""

            