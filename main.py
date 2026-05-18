#!/usr/bin/env python3
"""quote‑micro – print a random motivational quote.

Run: `python main.py`
"""
import random
import sys

# List of quotes (feel free to extend)
quotes = [
    "The only way to do great work is to love what you do. – Steve Jobs",
    "Believe you can and you're halfway there. – Theodore Roosevelt",
    "Success is not final, failure is not fatal: it is the courage to continue that counts. – Winston Churchill",
    "Don't watch the clock; do what it does. Keep going. – Sam Levenson",
    "The best time to plant a tree was 20 years ago. The second best time is now. – Chinese Proverb",
    "You miss 100% of the shots you don't take. – Wayne Gretzky",
    "Hard work beats talent when talent doesn't work hard. – Tim Notke",
]

def main():
    quote = random.choice(quotes)
    sys.stdout.write(quote + "\n")

if __name__ == "__main__":
    main()
