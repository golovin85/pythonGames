import random
import sys

def coin_toss():
    responses = [
        "Heads",
        "Tails",
        "Gone with the wind",
        "Oops! It landed on the edge!",
    ]

    print("Toss the coin")
    input("Ask a question: ")
    print("Tossing the coin...")
    print("And the result is:", random.choice(responses))

if __name__ == "__main__":
    coin_toss()
    input("Press Enter to exit.")
