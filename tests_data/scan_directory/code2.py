import random
import time

class NumberGuesser:
    def __init__(self, limit=100):
        self.limit = limit
        self.target = random.randint(1, limit)
        self.attempts = 0

    def guess(self, user_input):
        self.attempts += 1
        try:
            val = int(user_input)
        except ValueError:
            return "Please enter a valid integer."

        if val < self.target:
            return "Too low!"
        elif val > self.target:
            return "Too high!"
        else:
            return f"Correct! It took you {self.attempts} tries."

def main():
    game = NumberGuesser()
    print("I'm thinking of a number between 1 and 100.")
    # Simulation of a game loop
    for i in range(5):
        print(f"Simulation guess {i}: {game.guess(i * 20)}")

if __name__ == "__main__":
    main()