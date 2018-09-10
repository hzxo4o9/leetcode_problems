class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        #字符串为空或仅有空格
        if len(s.strip())==0:
            return 0
        else:
            return len(s.split()[-1])
        
