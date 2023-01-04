class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        self.t = t
        self.s = s
        pattern_list = list(t)
        string_list = list(s)
        x = []
        for i in pattern_list:
            if i not in x:
                x.append(i)
        res = []
        for i in pattern_list:
            res.append(x.index(i))

        y = []
        for i in string_list:
            if i not in y:
                y.append(i)
        res2 = []
        for i in string_list:
            res2.append(y.index(i))
        return res == res2
