import math
from typing import List

import numpy as np


class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        """
        https://leetcode.com/problems/stone-game-vi/

        There are n stones.
        Players take any stone in each turn and gain the points according to the stones index in their values.
        Alice starts.
        Both play optimally.

        The stones are not ordered, which is a very important pont.
        The value to each player is how much they gain plus how much they prevent the other player to gain by taking the stone.
        That is because the value taken by the other player is a stone that the first player has to gain elsewhere to win.
        So the game value of the stone i for Alice is F = aliceValues[i] + bobValue[i]

        Since the players play against each other. They always try to take the biggest game value.
        """

        # Alice and Bob results
        results = [0, 0]
        # Sort by the sum - the game value of the stone to each player.
        for i, value in enumerate(sorted(zip(aliceValues, bobValues), key=lambda x: x[0] + x[1], reverse=True)):
            # Assign to the player, who is on the turn.
            player_index = i % 2
            results[player_index] += value[player_index]

        return sign(results[0] - results[1])


def sign(a):
    return bool(a > 0) - bool(a < 0)




assert Solution().stoneGameVI(
    [69, 36, 42, 96, 61, 80, 74, 75, 75, 26, 34, 73, 22, 53, 13, 88, 73, 26, 78, 1, 12, 39, 51, 10, 21, 97, 85, 98, 41,],
    [73, 37, 39, 75, 98, 88, 53, 13, 96, 73, 51, 26, 92, 74, 75, 80, 69, 97, 1, 78, 85, 42, 34, 41, 48, 26, 12, 61, 10,]
) == 1

assert Solution().stoneGameVI(
    [69, 36, 42, 96, 61, 80, 74, 75, 75, 26, 34, 73, 22, 53, 13, 88, 73, 26, 78, 1, 12, 39, 51, 10, 21, 97, 85, 98, 41,
     92, 48, 37],
    [73, 37, 39, 75, 98, 88, 53, 13, 96, 73, 51, 26, 92, 74, 75, 80, 69, 97, 1, 78, 85, 42, 34, 41, 48, 26, 12, 61, 10,
     22, 21, 36]
) == 0
assert Solution().stoneGameVI([8], [8]) == 1
assert Solution().stoneGameVI([1,2], [3,1]) == 0
assert Solution().stoneGameVI([1, 3], [2, 1]) == 1
assert Solution().stoneGameVI([2,4,3], [1,6,7]) == -1
