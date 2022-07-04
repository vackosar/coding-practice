# https://leetcode.com/problems/simplify-path/submissions/
class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        Convert to cannonical path which starts at the root "/" and contains no '..' and '//' and does not end with a slash.
        While "..." is file or directory name. And going above root directory is no-op.

        Only special operation here is go up operation '..'. That can be served using a stack, while iterating.
        Time and space complexity will be linear.

        Read from the left, looking for a slash or end of string, then interpret buffer the contents, append to stask or pop from the stack.
        Ignore slashes.
        At the end, join entire stack with a slash, prepending slash at the left.


        # Solution reading character by character

        names = []
        buff = []
        for c in path + '/':
            if c == '/':
                if len(buff) == 0:
                    continue

                name = ''.join(buff)
                if name == '..':
                    if len(names) > 0:
                        names.pop()

                    buff = []
                    continue

                elif name == '.':
                    buff = []
                    continue

                else:
                    names.append(name)
                    buff = []
                    continue

            else:
                buff.append(c)

        return '/' + '/'.join(names)

        """

        names = []
        for name in path.split('/'):
            if len(name) == 0:
                continue

            elif name == '..':
                if len(names) > 0:
                    names.pop()

                continue

            elif name == '.':
                continue

            else:
                names.append(name)
                continue

        return '/' + '/'.join(names)