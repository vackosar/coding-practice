from typing import List


## Follow Vaclav Kosar for more software and machine learning at https://vaclavkosar.com/


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        current_combination = [0] * len(candidates)
        valid_combinations = set()
        if len(candidates) > 0:
            self.valid_combinations(candidates, current_combination, 0, 0, target, valid_combinations)
            return [list(combination) for combination in valid_combinations]

        else:
            return []

    def valid_combinations(self, candidates, current_combination, sum_val, pointer, target, valid_combinations):
        num = candidates[pointer]
        while sum_val <= target:
            if sum_val == target:
                valid_combination = []
                for i, val in enumerate(current_combination):
                    if val > 0:
                        valid_combination.extend([candidates[i]] * val)

                valid_combinations.add(tuple(valid_combination))

            if pointer + 1 < len(candidates):
                self.valid_combinations(candidates, current_combination, sum_val, pointer + 1, target,
                                        valid_combinations)

            sum_val = sum_val + num
            current_combination[pointer] += 1

        current_combination[pointer] = 0


assert Solution().combinationSum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]
