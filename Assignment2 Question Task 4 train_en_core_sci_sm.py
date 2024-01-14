import csv
import spacy
from transformers import BertTokenizer, BertForTokenClassification
from transformers import AutoTokenizer

with open('data.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    
# Split text into lines
lines = text.split('\n')

# Load SpaCy models
nlp_sci_sm = spacy.load('en_core_sci_sm')

# Process every 100,000 lines at a time
batch_size = 1000
all_entities_sci_sm = []

# CSV file setup
csv_file_sci_sm = 'output_entities_sci_sm.csv'

csv_columns = ['Text', 'Label']
# CSV file setup for 'en_core_sci_sm'
with open(csv_file_sci_sm, 'w', newline='', encoding='utf-8') as csvfile_sci_sm:
    csv_writer_sci_sm = csv.DictWriter(csvfile_sci_sm, fieldnames=csv_columns)
    csv_writer_sci_sm.writeheader()
    for i in range(0, len(lines), batch_size):
        batch = lines[i:i+batch_size]
        # Skip empty batches
        if not any(line.strip() for line in batch):
            continue
        # Join lines into a single text
        batch_text = '\n'.join(batch)
        # Extract entities using SpaCy 'en_core_sci_sm'
        doc_sci_sm = nlp_sci_sm(batch_text)
        entities_sci_sm = [(ent.text, ent.label_) for ent in doc_sci_sm.ents]
        all_entities_sci_sm.extend(entities_sci_sm)
        # Write entities to CSV
        for entity in entities_sci_sm:
            csv_writer_sci_sm.writerow({'Text': entity[0], 'Label': entity[1]})
            
# Print the extracted entities to the screen
print("Entities from 'en_core_sci_sm':", all_entities_sci_sm)