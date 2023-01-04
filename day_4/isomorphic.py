class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        self.t = t
        self.s = s
        t_list = list(t)
        s_list = list(s)
        x = []
        for i in t_list:
            if i not in x:
                x.append(i)
        res = []
        for i in t_list:
            res.append(x.index(i))

        y = []
        for i in s_list:
            if i not in y:
                y.append(i)
        res2 = []
        for i in s_list:
            res2.append(y.index(i))
        return res == res2
