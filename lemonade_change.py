from collections import defaultdict, Counter
from typing import List


## Follow Vaclav Kosar for more software and machine learning at https://vaclavkosar.com/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        """
        Each lemonade cost $5. Each customer wants to buy the lemonade and pay with 5, 10, or 20 dollar bill.
        You must provide the correct change to each in the order they come.
        You start without cash.

        Return True if you can provide the change to the customers described by `bills`.


        >>> Solution().lemonadeChange([5])
        True

        >>> Solution().lemonadeChange([10])
        False

        >>> Solution().lemonadeChange([5, 10])
        True

        >>> Solution().lemonadeChange([5, 20])
        False

        >>> Solution().lemonadeChange([5,5,5,10,20])
        True

        >>> Solution().lemonadeChange([5,5,10,10,20])
        False


        I don't think there is a faster way than to simulate the situation.
        This would mean complexity of O(N), O(N).

        Keep the change counter. For each bill find if you can return.
        There may be more than one change bill to return, and they may be values of 5 or 10.
        In total the change can be: 5 or 15 (5+5+5 or 10+5).

        There is additional complexity, where we can decide how we will return the bills.
        Greedy strategy of returning the biggest bills first gives us maximum possible actions for later.

        """
        change = Counter()
        # change = defaultdict(lambda: 0)

        for bill in bills:
            if bill == 5:
                # We have nothing to return.
                change[5] += 1

            elif bill == 10:
                if change[5] >= 1:
                    change[5] -= 1
                    change[10] += 1

                else:
                    return False

            elif bill == 20:
                # There is little point counting $20 bills beyond debugging, because we won't be returning them.
                if change[10] >= 1 and change[5] >= 1:
                    change[5] -= 1
                    change[10] -= 1
                    change[20] += 1

                elif change[5] >= 3:
                    change[5] -= 3
                    change[20] += 1

                else:
                    return False

            else:
                raise RuntimeError()

        return True