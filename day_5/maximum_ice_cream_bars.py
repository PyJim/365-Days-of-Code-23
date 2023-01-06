class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        self.coins = coins
        self.costs = costs
        costs.sort()
        total = 0
        answers = []
        for cost in costs:
            if total+cost <= coins:
                answers.append(cost)
                total += cost
        return len(answers)
