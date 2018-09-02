class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev = 0
        if x>0:
            while (x):
                a = x%10
                rev = rev*10+a
                x = x//10
            if (rev < pow(2,31)-1) :
                return rev
            else:
                return 0
            
        if x<0:
            x = abs(x)
            while (x):
                a = x%10
                rev = rev*10+a
                x = x//10
            if  (rev < pow(2,31)):
                 return -rev
            else:
                 return 0
        if x==0:
            return 0
                        
