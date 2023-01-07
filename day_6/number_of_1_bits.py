class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.n = n
        n = bin(n)[2:]
        return n.count("1")
