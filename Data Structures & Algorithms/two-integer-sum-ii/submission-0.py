class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            summ = numbers[l] + numbers[r]
            if summ == target:
                return[l+1,r+1]
            elif summ > target:
                r -= 1
            else:
                l +=1
        return [-1, -1]