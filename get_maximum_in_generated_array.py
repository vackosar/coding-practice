
## Follow me for more software and machine learning at https://vaclavkosar.com/


class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        """
        Given integer `n` return maximum `nums` array with the following properties: ```
            len(nums) == n + 1

            nums[0] = 0
            nums[1] = 1

            # The even numbers are equal to their index / 2 value
            nums[2 * i] = nums[i] for 2 <= 2 * i <= n

            # The odd numbers are bigger, they are sum of index / 2 and index / 2 + 1
            nums[2 * i + 1] = nums[i] + nums[i + 1] for 2 <= 2 * i + 1 <= n
        ```

        Return the maximum integer in the array `nums`.


        Let's take the first examples:

        >>> Solution().getMaximumGenerated(len([0]) - 1)
        0

        >>> Solution().getMaximumGenerated(len([0, 1]) - 1)
        1

        >>> Solution().getMaximumGenerated(len([0, 1, 1]) - 1)
        1

        >>> Solution().getMaximumGenerated(len([0, 1, 1, 2]) - 1)
        2

        >>> Solution().getMaximumGenerated(len([0, 1, 1, 2, 1]) - 1)
        2

        >>> Solution().getMaximumGenerated(len([0, 1, 1, 2, 1, 3]) - 1)
        3

        >>> Solution().getMaximumGenerated(len([0, 1, 1, 2, 1, 3, 2]) - 1)
        3


        >>> Solution().getMaximumGenerated(len([0, 1, 1, 2, 1, 3, 2, 3]))
        3

        >>> Solution().getMaximumGenerated(len([0, 1, 1, 2, 1, 3, 2, 3, 1]))
        4


        It should be possible to calculate this iteratively, but there likely is a formula for this based on index `i`.

        """

        if n == 0:
            return 0

        elif n == 1:
            return 1

        nums = [0, 1]
        i = 2
        max_val = 1

        while i <= n:
            if i % 2 == 0:
                last = nums[i // 2]

            else:
                last = nums[i // 2] + nums[i // 2 + 1]

            nums.append(last)
            i += 1
            if last > max_val:
                max_val = last

        return max_val






