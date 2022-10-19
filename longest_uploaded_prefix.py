from utils import call_with_inputs


class LUPrefix(object):
    """
    Input is a stream of n videos represented by an index of 1, 2, ..., n - 1, n.
    Upload the videos to server.
    Given the uploaded indexes at this point, return the longest consecutive sequence of ids starting from 1.

    Need to keep a memory of what we have seen.

    # Brute force
    On every longest call through the array to calculate the prefix.

    # Memoization
    Keep the last prefix position and on adding the next adjacent video continue to find new prefix.

    """

    def __init__(self, n):
        """
        :type n: int
        """
        self.uploaded = [False] * (n + 1)
        self.prefix = -1

    def upload(self, video):
        """
        :type video: int
        :rtype: None
        """
        new_i = video - 1
        self.uploaded[new_i] = True
        if new_i == self.prefix + 1:
            i = new_i
            for i in range(new_i, len(self.uploaded)):
                if not self.uploaded[i]:
                    break

            self.prefix = i - 1

    def longest(self):
        """
        :rtype: int
        """
        return self.prefix + 1


call_with_inputs(
    LUPrefix(4),
    ["upload", "longest", "upload", "longest", "upload", "longest"],
    [[3], [], [1], [], [2], []],
    [None, 0, None, 1, None, 3]
)

