import random
from collections import defaultdict

# Step 1: Read the lyrics from text file and clean it
with open('lyrics.txt', 'r') as file:
    lyrics = file.read().replace('\n', ' ').replace('\r', ' ')  # Clean newlines and carriage returns

# Step 2: Tokenize the lyrics into words
words = lyrics.strip().split()

# Step 3: Build the Markov Chain (Bigram model - current word -> next word)
markov_chain = defaultdict(list)

for current_word, next_word in zip(words[:-1], words[1:]):
    markov_chain[current_word].append(next_word)

# Step 4: Generate lyrics using the Markov Chain
def generate_lyrics(chain, start_word, length=30):
    word = start_word
    lyrics_generated = [word]

    for _ in range(length - 1):
        next_words = chain.get(word)
        if not next_words:  # If no words follow the current word, break
            break
        word = random.choice(next_words)  # Choose a random next word
        lyrics_generated.append(word)

    return ' '.join(lyrics_generated)

# Step 5: Generate new lyrics
start_word = random.choice(words)  # Randomly select a word to start
new_lyrics = generate_lyrics(markov_chain, start_word, length=30)

print("🎤 AI-Generated Lyrics:")
print(new_lyrics)
