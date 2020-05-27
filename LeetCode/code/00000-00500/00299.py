class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        count_a = 0
        count_b = 0
        secret_dict = dict()
        guess_dict = dict()
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                count_a += 1
            else:
                secret_dict[secret[i]] = secret_dict.get(secret[i], 0) + 1
                guess_dict[guess[i]] = guess_dict.get(guess[i], 0) + 1
        for key in secret_dict.keys():
            if key in guess_dict:
                count_b += min(secret_dict[key], guess_dict[key])
        return str(count_a) + 'A' + str(count_b) + 'B'
