
## Follow Vaclav Kosar for more software and machine learning at https://vaclavkosar.com/

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        """
        Given path, where each character represents direction of movement ( `path[i] in ['N', 'S', 'E', 'W']`) and you start at (0, 0).
        Return True if path crosses itself, otherwise False.

        Since we make single step that means revisiting any previous node.


        >>> Solution().isPathCrossing('NES')
        False

        >>> Solution().isPathCrossing('NESWW')
        True


        Simplest solution is walk the path, and record all locations, check when we are revisiting.
        This is O(N) solution in path and memory.

        """

        visited = set()

        x_position = 0
        y_position = 0
        visited.add((x_position, y_position))

        for c in path:
            if c == 'N':
                y_position += 1

            elif c == 'S':
                y_position -= 1

            elif c == 'E':
                x_position -= 1

            elif c == 'W':
                x_position += 1

            else:
                raise RuntimeError()

            if (x_position, y_position) in visited:
                return True

            visited.add((x_position, y_position))

        return False

