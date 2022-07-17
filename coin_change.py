from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """

        Return fewest coins that make us the amount. If it is impossible, return -1.
        Coins list specificy the denominations of which you have infinite instances.

        # Dynamic Programming With Memorization
        This can be solved via dynamic programming.
        We could build up to the desired amount step by step, while remembering how many coins where required.
        Eventually we get to desired amount.

        """

        # We will iteratively solve for smaller amount that the target.
        amounts = [-1] * (amount + 1)

        # The solution for zero is 0.
        amounts[0] = 0

        # Sorting coins will give us small speedup at the beginning of the search.
        coins.sort()

        # Let's iterate over the amounts, using the previous solutions.
        for current_amount in range(1, amount + 1):
            for coin in coins:
                previous_amount = current_amount - coin
                if current_amount - coin < 0:
                    # this coin is too big already, no point trying bigger.
                    break

                # Did we solve this amount previously?
                if amounts[previous_amount] > -1:
                    # Let's try if we can improve the current best solution with using this coin.
                    # Note that, here just the size of the coin will not tell us that it is the best solution, we really have to try.
                    if amounts[current_amount] == -1 or amounts[previous_amount] + 1 < amounts[current_amount]:
                        amounts[current_amount] = amounts[previous_amount] + 1

        return amounts[amount]


assert Solution().coinChange([1, 2, 5], 6) == 2
assert Solution().coinChange([1, 2, 5], 11) == 3
assert Solution().coinChange([186, 419, 83, 408], 6249) == 20

"""
        # Failed Attempt at a Greedy Solution
        So decompose amount = n1 * coin1 + n2 * coin2 + ... + nM * coinM.
        Greedy approach would be to start with the maximum coin and maximum count.
        If I cannot fit the amount, I would then start with the next biggest coin.
        But the reminder may nto be decomposable.
        In case of `[2, 5], 16`, I can fit only 2*5 and use 3*2. Greedy would fail here.
        I would have to know ahead, when I am having this problem.
        Also, I must know what numbers I cannot generate at all quickly.
        In above, I cannot generate `[1, 3, 11, 13, 21, 23]`, while non-greedy are `[6, 8, 16, 28] = 5 + [1, 3, 11, 13, 21, 23]`.
        This may mean that, that unexpressable sequence starting from 1, will generate non-greedy cases,
        by adding combinations, until it overflows. So I could test for non-greedy if I have the unsolvable sequence.
        Unsolvable sequence is given by numbers between 1 and max(coins), and then can be generated, but how?
        For `[3, 5]` its `[1, 2, 4, 6, 7, 9, 11]= [1,2,4,5+1,5+2,5+4,...`.
"""
