class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Robot visiting m x n grid. Starts at top-left 0, 0. Goal is at bottom-right m-1, n-1.
        Allowed steps is down or right.

        Given the grid, return the number of possible paths that robot can take to the goal position.

        # Brute Force
        Depth first search of all possible paths with e.g. recursion.
        Problem of recursion is that we recalculate many fields again, and thus we increase complexity.
        Complexity of this solution is exponential O(2**(M * N)) time and O(M*N) space.
        Instead it is better to keep subproblem solutions in memory with dynamic programming solution.

        # Note that you can store your solutions in the paths array. Uncomment to try that.
        # self.paths = []
        self.n_paths = 0
        self.m = m
        self.n = n

        def step(self, i: int, j: int, path: list):
            if i == self.m - 1 and j == self.n - 1:
                self.n_paths += 1
                # self.paths.append(path.copy())
                return


            if i < self.m - 1:
                # path.append(1)
                self.step(i+1, j, path)
                # path.pop(-1)

            if j < self.n - 1:
                # path.append(0)
                self.step(i, j+1, path)
                # path.pop(-1)


            return

        path = []
        step(0, 0, path)
        # print(self.paths)
        return self.n_paths


        # Dynamic Programming Memoization
        Let's start from the goal position and calculate back memorizing the path counts instead.
        This reduces time to linear complexity, as we don't recalculate what we already visited.
        We always need to have previous row results available to calculate the current row.
        So, memory complexity of this solution can be further reduced by only remembering the current row and previous row to O(M).
        """

        self.m = m
        self.n = n

        self.n_paths = [([0] * self.n) for _ in range(self.m)]
        for diff_i in range(self.m):
            for diff_j in range(self.n):
                i = self.m - 1 - diff_i
                j = self.n - 1 - diff_j

                n_paths_from_here = 0

                if i < self.m - 1:
                    n_paths_from_here += self.n_paths[i + 1][j]

                if j < self.n - 1:
                    n_paths_from_here += self.n_paths[i][j + 1]

                if i == self.m - 1 and j == self.n - 1:
                    n_paths_from_here = 1

                self.n_paths[i][j] = n_paths_from_here

        return self.n_paths[0][0]


"""
Like and follow me at https://vaclavkosar.com/

Additional Solutions:
https://leetcode.com/problems/unique-paths/discuss/254228/Python-3-solutions%3A-Bottom-up-DP-Math-Picture-Explained-Clean-and-Concise
"""
