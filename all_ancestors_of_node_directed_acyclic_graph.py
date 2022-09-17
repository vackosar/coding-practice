from typing import List


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        """
        https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/
        
        Given number of nodes n and list of edges (from, to) connecting them, such that the network is directed acyclic graph.
        Return list of ancestor_sets for all nodes, such that they are sorted in ascending order according to their id.
        Note that it is not guaranteed that from <= to!


        # DFS O(N**2) Solution
        Kudos https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/discuss/1821935/Python3-Java-C%2B%2B-Simple-DFS-O(n-2)

        direct_child = defaultdict(list)
        ancestor_sets = [[] for _ in range(n)]
        for x, y in edges:
            direct_child[x].append(y)

        def dfs(dfs_start_node, current_node):
            for child in direct_child[current_node]:
                ancestors = ancestor_sets[child]
                if ancestors and ancestors[-1] == dfs_start_node:
                    continue

                ancestors.append(dfs_start_node)
                dfs(dfs_start_node, child)

        for i in range(n): dfs(i, i)
        return ancestor_sets


        # BFS Solution

        Important is to only append to the queue once the last parent of the child visited.
        """

        parent_lists = [[] for _ in range(n)]
        children_lists = [[] for _ in range(n)]
        for parent, child in edges:
            parent_lists[child].append(parent)
            children_lists[parent].append(child)

        roots = [node for node, parents in enumerate(parent_lists) if len(parents) == 0]
        ancestor_sets = [set() for _ in range(n)]

        bfs_to_visit_queue = roots
        while len(bfs_to_visit_queue) > 0:
            parent: int = bfs_to_visit_queue.pop(0)
            children = children_lists[parent]
            for child in children:
                ancestors = ancestor_sets[child]
                ancestors.add(parent)
                ancestors.update(ancestor_sets[parent])
                parent_list = parent_lists[child]
                parent_list.remove(parent)
                if len(parent_list) == 0:
                    # makes sure that the child is added only once into the queue
                    bfs_to_visit_queue.append(child)

        # Sets that keep sort may be better, but won't win if you implement them in Python, so we have to sort everything.
        return [list(sorted(a)) for a in ancestor_sets]


assert (Solution().getAncestors(8, [[0, 3], [0, 4], [1, 3], [2, 4], [2, 7], [3, 5], [3, 6], [3, 7], [4, 6]]) == [[], [], [], [0, 1], [0, 2], [0, 1, 3], [0, 1, 2, 3, 4], [0, 1, 2, 3]])
# Follow me at https://vaclavkosar.com/