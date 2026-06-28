import random

class GuessGame:
    def __init__(self, min_num=1, max_num=100):
        self.min_num = min_num
        self.max_num = max_num
        self.secret = random.randint(min_num, max_num)
        self.attempts = 0

    def guess(self, number):
        self.attempts += 1
        if number < self.secret:
            return -1
        elif number > self.secret:
            return 1
        else:
            return 0

    def reset(self, min_num=None, max_num=None):
        if min_num is not None:
            self.min_num = min_num
        if max_num is not None:
            self.max_num = max_num
        self.secret = random.randint(self.min_num, self.max_num)
        self.attempts = 0