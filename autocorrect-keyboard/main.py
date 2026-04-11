import nltk
from nltk.util import ngrams
from collections import Counter
from textblob import TextBlob

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('gutenberg')

from nltk.corpus import gutenberg

# Load dataset
text = gutenberg.raw('austen-emma.txt')
tokens = nltk.word_tokenize(text.lower())

# Create bigrams
bigrams = list(ngrams(tokens, 2))
bigram_freq = Counter(bigrams)

# Autocorrect function
def autocorrect(sentence):
    return str(TextBlob(sentence).correct())

# Prediction function
def predict_next_word(word):
    candidates = [pair for pair in bigram_freq if pair[0] == word.lower()]
    
    if not candidates:
        return "No prediction"
    
    return max(candidates, key=lambda pair: bigram_freq[pair])[1]

# Main program
user_input = input("Enter a sentence: ")

# Step 1: Autocorrect
corrected = autocorrect(user_input)
print("Corrected:", corrected)

# Step 2: Prediction
last_word = corrected.split()[-1]
prediction = predict_next_word(last_word)

print("Next word:", prediction)