class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if (x<0):
            return False
        if(x//10==0):
            return True
        if (x>0):
            x = list(str(x))
            x=[int(i) for i in x]
            for i in range(0,len(x)//2):
                if(x[i] != x[len(x)-1-i]):
                    return False
                
            return True
        #各种情况要考虑清楚，负数，正数，个位数整数等。
            
