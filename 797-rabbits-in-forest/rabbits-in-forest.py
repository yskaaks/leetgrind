class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counter = collections.Counter(answers)
        res = 0
        for answer, count in counter.items():

            groups = math.ceil(count/(answer+1))

            res += groups *(answer+1)
        return res