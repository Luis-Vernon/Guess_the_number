import random

class GuessGame:
    def __init__(self, min_num=1, max_num=100):
        self.min_num = min_num
        self.max_num = max_num
        self.secret = random.randint(min_num, max_num)
        self.attempts = 0

    def guess(self, number):
        """Возвращает -1 если меньше, 0 если угадал, 1 если больше."""
        self.attempts += 1
        if number < self.secret:
            return -1
        elif number > self.secret:
            return 1
        else:
            return 0

    def reset(self):
        self.secret = random.randint(self.min_num, self.max_num)
        self.attempts = 0