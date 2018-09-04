class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        s = list(s)
        sum = 0
        for i in range(len(s)-1):
            if dict[s[i]]>=dict[s[i+1]]:
                sum = dict[s[i]]+sum
            if dict[s[i]]<dict[s[i+1]]:
                sum = sum-dict[s[i]]
        sum = sum +dict[s[-1]]
                
        return sum
        
