class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for number in nums:
            if number in frequency:
                frequency[number] += 1
            else:
                frequency[number] = 1
        sorted_numbers = sorted(
            frequency,
            key=frequency.get,
            reverse=True
        )

        return sorted_numbers[:k]
