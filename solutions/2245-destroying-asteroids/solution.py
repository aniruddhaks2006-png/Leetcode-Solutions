class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        cnt = [0] * 100001

        for a in asteroids:
            cnt[a] += 1

        for value in range(1, 100001):
            while cnt[value]:
                if value > mass:
                    return False
                mass += value
                cnt[value] -= 1

        return True
