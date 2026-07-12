from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = Counter(nums)

        freq_list = [[] for _ in range(len(nums) + 1)]

        for num, count in count.items():
            freq_list[count].append(num)
        
        r = []

        for i in range(len(freq_list) - 1, 0, -1):

            for num in freq_list[i]:
                r.append(num)
                if len(r) == k:
                    return r