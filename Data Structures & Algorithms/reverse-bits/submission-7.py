class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32): #0 -> 31 (32 iterations)
            bit = (n >> i) & 1
            res |= bit << (31 - i)

        return res