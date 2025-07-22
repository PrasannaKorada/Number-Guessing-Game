# 🎯 Python Number Guessing Game

A simple command-line based number guessing game developed in Python.  
The user must guess a randomly generated number within a given range.  
The game provides helpful hints after each guess and tracks the number of attempts.

---

## 🚀 How It Works

1. User inputs the **lowest** and **highest** numbers for the guessing range.
2. The program randomly generates a secret number within this range.
3. User keeps guessing until they find the correct number.
4. After each guess:
   - If out of range → warning is shown.
   - If too low/high → hints are given.
   - If correct → game ends with congratulations and guess count.

---

## 🧠 Features

- ✅ Range selection (custom start & end)
- ✅ Tracks number of guesses
- ✅ Input validation (digits only)
- ✅ Hint system (too high / too low)
- ✅ Graceful handling of invalid input

---

## 🛠️ Tech Stack

- Python 3
- No external libraries needed

---

## ▶️ How to Run

```bash
python number_guessing_game.py
