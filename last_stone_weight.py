from typing import List


# Follow Vaclav Kosar for more software and machine learning at https://vaclavkosar.com/


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        You are given stones list of weights of stones.
        In each turn choose heaviest 2 stones (x<=y) and smash them.
        If x==y: both are destroyed
        If x!=y: y has a weight of y-x, x is destroyed.
        Iterate.
        Return the weight of the final stone left or zero if there is none left.


        # 3-2=1, 1-1, 0
        >>> Solution().lastStoneWeight([1, 2, 3])
        0

        >>> Solution().lastStoneWeight([3,2,1])
        0

        >>> Solution().lastStoneWeight([3,1])
        2

        >>> Solution().lastStoneWeight([1])
        1

        # 8-7=1, 4-2=2, [2,1,1,1], [1,1,1], ...
        Solution.lastStoneWeight([2,7,4,1,8,1])
        1

        The simplest is to simulate the process.
        First sort, then pop 2, push back substraction.
        So the best datastructure is a heap for this.

        Time complexity thanks to heap sort is O(N Log N). Space, because of the need to copy the list, is O(N), but could be O(1).

        """

        import heapq

        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            s1 = heapq.heappop(stones)
            s2 = heapq.heappop(stones)
            s3 = s1 - s2
            if s3 != 0:
                heapq.heappush(stones, s3)

        if len(stones) == 0:
            return 0

        else:
            return -heapq.heappop(stones)
