from Live import load_game, welcome
from GuessGame import play as guess_play
from MemoryGame import play as memory_play
from CurrencyRouletteGame import play as CurrencyRoulette_play
print(welcome("Guy"))
game_choice, game_difficulty = load_game()

# "1. Memory Game ", "2. Guess Game", "3. Currency Roulette"
if game_choice == "1":
    memory_play(int(game_difficulty))
elif game_choice == "2":
    guess_play(int(game_difficulty))
elif game_choice == "3":
    CurrencyRoulette_play()
