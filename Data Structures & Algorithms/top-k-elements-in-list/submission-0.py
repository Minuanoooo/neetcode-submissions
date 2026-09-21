class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counts = {}
        for item in nums:
            counts[item] = counts.get(item, 0) + 1
        result = []
        for i in range(k):
            most_frequent_item = max(counts, key=counts.get)
            result.append(most_frequent_item)
            del counts[most_frequent_item]
        return result
