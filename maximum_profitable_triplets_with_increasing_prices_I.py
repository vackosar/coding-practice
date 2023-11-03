from typing import List

## Follow Vaclav Kosar for more software and machine learning at https://vaclavkosar.com/

class Solution:
    def maxProfit(self, prices: List[int], profits: List[int]) -> int:
        """
        Given prices and profits for items, pick 3 items satisfying below with the highest sum of profits.

        (prices[i] < prices[j] < prices[k]) and i < j < k

        The profit is profits[i] + profits[j] + profits[k].

        Return the sum of the profits or return -1.


        # Examples with Edge Cases

        I need to test the cases around the boundary of the conditions.

        Less than 3 elements
        >>> Solution().maxProfit([0, 1], [1, 1])
        -1

        Empty
        >>> Solution().maxProfit([], [])
        -1

        Select the biggest
        >>> Solution().maxProfit(prices = [10,2,3,4], profits = [10,2,3,4])
        9

        Select the biggest
        >>> Solution().maxProfit(prices = [1,2,3,4,5], profits = [1,5,3,4,6])
        15

        Select the biggest
        >>> Solution().maxProfit(prices = [4,3,2,1], profits = [33,20,19,87])
        -1


        # Reasoning about Radical Solution Approaches To Find The Best One Of The Correct

        Brute force is O(N**3).
        Faster is greedy the biggest 3 numbers search and using a heap.
        Iteratively filtering to an option that will satisfy the condition.
        Both price and position of the item in the array limits viable selection of additional items on the left (partial order).
            A number that is bigger to the left may have more options, because it may select bigger numbers.
            If the number is more on the right despite being smaller it may have more options than the bigger number.
            But if it is more on the right and bigger, then it has always more options.
            I could use this to limit the search space, but it is not helping me much now.

        Let's go back. There is dependency between `i` and `j`, and also j and k. So knowing j in O(N), I can search i and k in O(N), leading to O(N**2).
        In the future, additional improvements can be achieved with sorting first by the most impactful filter, which seems to be the prices, then sort by profits in the second priority.


        # Critical points of risk or misunderstanding

        Not satisfying the condition of increasing consecutive prices.
        I will be searching twice, so I will make sure I will use the right boundaries, rewrite variables correctly and completely.


        # Correct and Complete Implementation

        """

        max_profit = -1
        for j in range(len(prices)):
            max_i_profit = -1
            for i in range(j):
                if prices[i] < prices[j] and profits[i] > max_i_profit:
                    max_i_profit = profits[i]

            if max_i_profit == -1:
                continue

            max_k_profit = -1
            for k in range(j + 1, len(prices)):
                if prices[k] > prices[j] and profits[k] > max_k_profit:
                    max_k_profit = profits[k]

            if max_k_profit == -1:
                continue

            if max_i_profit + profits[j] + max_k_profit > max_profit:
                max_profit = max_i_profit + profits[j] + max_k_profit

        return max_profit

        """
        
        # Applications of The Principles Of The Solution 
        
        This method can be used anywhere where we have to search for triples, that depend only on one of the items.
        """
