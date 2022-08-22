from typing import List


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        """
        Each house can be warmed if within the radius.
        Houses and heaters are on a line described by inputs.

        Input is coordinates of houses and heaters on a line in a sorted order.
        Return minimum radius of heaters to cover all houses given the input.


        The biggest distance to closest heater gives me the radius.
        To speed up the solution, I keep the two heaters. The current and the next.
        As long as the houses I iterate on are closer to the first heater, I keep measuring the distance to the first.
        If the next one is the same distance or closer, I keep moving forward with the heater iterator.
        """

        houses.sort()
        heaters.sort()

        heaters_iter = iter(heaters)
        heater = next(heaters_iter)
        next_heater = next(heaters_iter, None)

        def set_next_heater():
            nonlocal heaters_iter, next_heater, heater
            if next_heater is not None:
                heater = next_heater
                next_heater = next(heaters_iter, None)

        total_max_dist = 0
        for house in houses:
            dist = abs(house - heater)
            if next_heater:
                next_dist = abs(house - next_heater)
                min_dist = min(dist, next_dist)
                while dist >= next_dist:
                    set_next_heater()
                    if next_heater is None:
                        break

                    dist = next_dist
                    next_dist = abs(house - next_heater)
                    min_dist = min(dist, next_dist)

                total_max_dist = max(min_dist, total_max_dist)

            else:
                min_dist = dist
                total_max_dist = max(min_dist, total_max_dist)

        return total_max_dist

# Upvote and consider following me at https://vaclavkosar.com/


assert Solution().findRadius(
    [1, 1, 1, 1, 1, 1, 999, 999, 999, 999, 999],
    [499, 500, 501]
) == 498
assert Solution().findRadius([1, 2, 3, 4], [1, 4]) == 1


