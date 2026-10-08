class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        solution = []
        numbers = set(nums)
        for number in numbers:
            if target-number in numbers:
                if(number == target-number):
                    if(nums.count(number) == 1):
                        continue
                    solution.append(nums.index(number))
                    solution.append(nums.index(target-number,nums.index(number)+1))
                    solution.sort()
                    return solution
                solution.append(nums.index(number))
                solution.append(nums.index(target-number))
                solution.sort()
                return solution
        return solution
        