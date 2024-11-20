import random
import time
import threading


class ClickTheRightKeyGame:
    def __init__(self):
        self.target_key = None
        self.start_time = None
        self.score = 0
        self.time_limit = 3  # Time limit in seconds

    def generate_random_key(self):
        self.target_key = random.choice("abcdefghijklmnopqrstuvwxyz")
        return self.target_key

    def start_game(self):
        rounds = 5  # Number of rounds
        self.score = 0

        for round_number in range(1, rounds + 1):
            self.play_round(round_number)

        print(f"\nGame Over! Your final score: {self.score}/{rounds}")

    def play_round(self, round_number):
        print(f"\nRound {round_number} of 5!")
        target_key = self.generate_random_key()
        print(f"Press the key: {target_key.upper()}")

        self.start_time = time.time()
        user_input = None

        # Start a thread to listen for user input with a timeout
        def get_input():
            nonlocal user_input
            user_input = input("Your input: ").strip().lower()

        input_thread = threading.Thread(target=get_input)
        input_thread.daemon = True
        input_thread.start()

        # Wait for input or timeout
        input_thread.join(timeout=self.time_limit)

        self.end_time = time.time()

        # Check results
        if user_input == "exit":
            print("You exited the game.")
            exit()

        if not user_input:
            print("Time's up! You didn't press any key.")
        elif user_input == target_key:
            reaction_time = self.end_time - self.start_time
            print(f"Correct! Your reaction time: {reaction_time:.2f} seconds.")
            self.score += 1
        else:
            print(f"Wrong key! The correct key was '{target_key.upper()}'.")
