class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        bulls = 0
        cows = 0

        secret = list(secret)
        guess = list(guess)

        # Count bulls
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
                secret[i] = '#'
                guess[i] = '*'

        # Count cows
        for i in range(len(guess)):
            if guess[i] in secret:
                cows += 1
                secret[secret.index(guess[i])] = '#'

        return str(bulls) + "A" + str(cows) + "B"
