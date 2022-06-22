import heapq
from typing import List


class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        """
        2d interger array, orders[i] = [price, amount, orderType]
        order type: 0 buy, 1 sell
        keep 2 lists such that ordered by price
        Always consume from

        Keep ordered lists. Ideal is heap, bc it has fast insert and pop.
        Ideally the earlier orders would get matched first.

        """
        buys = []
        sells = []

        for i, order in enumerate(orders):
            if order[2] == 0:
                # buy
                self.annihilate(order, sells)
                if order[1] > 0:
                    heapq.heappush(buys, (-order[0], i, order))

            else:
                self.annihilate(order, buys)
                if order[1] > 0:
                    heapq.heappush(sells, (order[0], i, order))

        r = sum(order[2][1] for order in sells + buys)
        return r % (10**9 + 7)

    def annihilate(self, order, sells_or_buys: list):
        while order[1] > 0 and len(sells_or_buys) > 0 and (
                (order[2] == 0 and order[0] >= sells_or_buys[0][2][0])
                or (order[2] == 1 and order[0] <= sells_or_buys[0][2][0])):
            match = heapq.heappop(sells_or_buys)
            match_order = match[2]
            if order[1] == match_order[1]:
                match_order[1] = 0
                order[1] = 0
                break

            elif order[1] > match_order[1]:
                order[1] -= match_order[1]
                match_order[1] = 0

            elif order[1] < match_order[1]:
                match_order[1] -= order[1]
                order[1] = 0
                heapq.heappush(sells_or_buys, match)
                break


assert Solution().getNumberOfBacklogOrders([[7, 1000000000, 1], [15, 3, 0], [5, 999999995, 0], [5, 1, 1]]) == 999999984
assert Solution().getNumberOfBacklogOrders([[10, 5, 0], [15, 2, 1], [25, 1, 1], [30, 4, 0]]) == 6
