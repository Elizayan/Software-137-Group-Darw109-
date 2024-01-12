import csv
import re
from collections import Counter
#read the file
with open('new_TEXT', 'r', encoding='utf-8') as file:
    text = file.read()
#get all of the word
english_words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
#words count
word_counts = Counter(english_words)
#find out the 30 most common words
top_30_words = word_counts.most_common(30)
#save them into the csv file
csv_file_path = 'top_30_words.csv'
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Word', 'Count'])  
    for word, count in top_30_words:
        print(f'{word}: {count}')
        csv_writer.writerow([word, count])