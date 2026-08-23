class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2
        left_sum = 0
        right_sum = 0
        left_q = 0
        right_q = 0
        for i in range(n):
            if num[i] == '?':
                if i < half:
                    left_q += 1
                else:
                    right_q += 1
            elif i < half:
                left_sum += int(num[i])
            else:
                right_sum += int(num[i])
        if (left_q - right_q) % 2:
            return True
        return left_sum - right_sum != 9 * (right_q - left_q) // 2
