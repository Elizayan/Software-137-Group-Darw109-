#task 3.2

import nltk
import csv
from collections import Counter
from nltk.corpus import stopwords
from nltk import wordpunct_tokenize
from transformers import AutoTokenizer

# Download NLTK resources if not already downloaded
nltk.download('stopwords')

# Get a set of English stopwords
stop_words = set(stopwords.words('english'))

def is_english_word(word):
    # Check if the word is not a stopword and contains only alphabetic characters
    return word.lower() not in stop_words and word.isalpha()

def count_unique_english_tokens(text, model_name):
    # Load the tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    # Tokenize the text
    tokens = wordpunct_tokenize(text)
    # Filter out non-English words
    english_tokens = [token for token in tokens if is_english_word(token)]
    # Count the occurrences of each English token
    token_counts = Counter(english_tokens)
    # Get the top 30 English tokens
    top_30_tokens = token_counts.most_common(30)
    return top_30_tokens

text_file_path = 'data.txt'
with open(text_file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# You can replace this with the desired tokenizer model name
model_name = 'bert-base-uncased'  
top_30_english_tokens = count_unique_english_tokens(text, model_name)

# Print the top 30 English tokens
csv_file_path = 'top_30_words_nltk.csv'
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Word', 'Count']) 
    for word, count in top_30_english_tokens:
        print(f'{word}: {count}')
        csv_writer.writerow([word, count])