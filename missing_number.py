from typing import List


## Follow Vaclav Kosar for more software and machine learning at https://vaclavkosar.com/


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        Return the missing number from range 0 to len(nums).


        ## Examples

        >>> Solution().missingNumber([0, 3, 1])
        2

        >>> Solution().missingNumber([1, 0])
        2


        ## Correct Solution

        Brute for is to iterate and check presence of each number. But that would be O(N**2).

        An alternative is to sort first, then do halving to find the missing number for O(N*log(N)).


        ## Alternative

        One could quicksort and search the number at the same time, but that would be complicated.


        ## Avoid Mistakes

        Avoid +1 differences. Avoid unusual inputs errors.
        The array cannot be empty.
        Check the boundary indexes first, otherwise the halfing will not find missing indexes there.


        ## Implementation

        """

        # Quick sort
        nums.sort()

        # Check the boundaries
        left = 0
        right = len(nums) - 1

        if nums[left] > 0:
            return 0

        if nums[right] < len(nums):
            return len(nums)

        # Halving to find the missing number in the middle.
        while True:
            middle = (left + right) // 2
            # Example: [0, 1, 3]. middle == 1. nums[middle] == 1. Then go right.
            if nums[middle] > middle:
                # go left
                right = middle

            else:
                # go right
                left = middle

            # Example. left==1 and right==2, nums[left]==1
            if left + 1 == right:
                return nums[left] + 1

