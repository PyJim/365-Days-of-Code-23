class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        self.strs = strs
        count = 0
        answer = 0
        while count < len(strs[0]):
            items = []
            for i in strs:
                items.append(i[count])
            new_items = list(items)
            new_items.sort()
            if items != new_items:
                answer += 1
            count += 1
        return answer

#JEK __python__