class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        J = list(J)
        S = list(S)
        num = 0
        for i in J:
            for j in range(len(S)):
                if S[j] == i:
                    num=num+1
                else:
                    pass
        return num
     #可以了解count()函数，用于统计字符串里某个字符出现的次数。
