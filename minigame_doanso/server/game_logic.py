import random
from config import MIN_NUMBER, MAX_NUMBER

class GuessGame:
    def __init__(self):
        self.reset_game()

    def reset_game(self):
        self.target = random.randint(MIN_NUMBER, MAX_NUMBER)
        self.active = True
        print(f"[GAME] 🎯 Số mới của trò chơi là: {self.target}")

    def check_guess(self, number):
        if number < self.target:
            return "LOW"
        elif number > self.target:
            return "HIGH"
        else:
            return "WIN"
