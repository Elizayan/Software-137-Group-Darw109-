import csv
import spacy
import scispacy
from transformers import BertTokenizer, BertForTokenClassification
from transformers import AutoTokenizer
from spacy.lang.en import English
from spacy.language import Language
from spacy.tokens import Doc
from spacy.training import Example
TRAIN_DATA = [
    ("Who is Shaka Khan?", {"entities": [(7, 17, "PERSON")]}),
    ("I like London and Berlin.",  {"entities": [(7, 13, "LOC"), (18, 24, "LOC")]}),
    ("You like Paris and Prague.", {"entities": [(9, 14, "LOC"), (19, 25, "LOC")]}),
]

def make_nlp(model_dir):
    # ORIGINALLY: Test that we can get confidence values out of the beam_ner pipe
    nlp = English()
    config = { "beam_width": 32, "beam_density": 0.001 }
    ner = nlp.add_pipe("beam_ner", config=config)
    train_examples = []
    for text, annotations in TRAIN_DATA:
        train_examples.append(Example.from_dict(nlp.make_doc(text), annotations))
        for ent in annotations.get("entities"):
            ner.add_label(ent[2])
    optimizer = nlp.initialize()
    # update once
    losses = {}
    nlp.update(train_examples, sgd=optimizer, losses=losses)
    # save
    #if not model_dir.exists():
    #model_dir.mkdir()
    nlp.to_disk(model_dir)
    print("Saved model to", model_dir)
    return nlp
 
def test_beam(nlp, text):
    # Report predicted entities using the beam search (beam_width 16 or higher)
    ner = nlp.get_pipe("beam_ner")

    # Get the prediction scores from the beam search
    doc = nlp.make_doc(text)
    docs = [doc]
    # beams = StateClass returned from ner.predict(docs)
    beams = ner.predict(docs)

    # Show individual entities and their scores as reported
    scores = ner.scored_ents(beams)[0]
    offsets=[]
    final_score=[]
    for ent, sco in scores.items():
        tok = doc[ent[0]]
        lbl = ent[2]
        spn = doc[ent[0]: ent[1]]     
        offsets.append(tok.idx)
        final_score.append(sco)      
    return (offsets,final_score)

with open('data.txt', 'r', encoding='utf-8') as file:
    text = file.read()

TEST_TEXT = "I like London and Paris."
MODEL_DIR = "./test_model"
# Split text into lines
lines = text.split('\n')

# Load SpaCy models
nlp_ner_bc5cdr_md = spacy.load('en_ner_bc5cdr_md', disable=["tok2vec", "tagger", "parser", "attribute_ruler", "lemmatizer"], exclude=["ner"])
# source NER from the same pipeline package as the last component
nlp_ner_bc5cdr_md.add_pipe("ner", source=spacy.load("en_ner_bc5cdr_md"))
# insert the entity ruler
nlp_ner_bc5cdr_md.add_pipe("entity_ruler", before="ner")

# Process every 100,000 lines at a time
batch_size = 100
all_entities_ner_bc5cdr_md = []

# CSV file setup
csv_file_ner_bc5cdr_md = 'output_entities_ner_bc5cdr_md.csv'
csv_columns = ['Text', 'Label', 'Score']
nlp = spacy.load('en_core_web_lg')
entities_ner_bc5cdr_md=[]
# nlp = make_nlp(MODEL_DIR)
# nlp = spacy.load(MODEL_DIR)
# CSV file setup for 'en_ner_bc5cdr_md'
with open(csv_file_ner_bc5cdr_md, 'w', newline='', encoding='utf-8') as csvfile_ner_bc5cdr_md:
    csv_writer_ner_bc5cdr_md = csv.DictWriter(csvfile_ner_bc5cdr_md, fieldnames=csv_columns)
    csv_writer_ner_bc5cdr_md.writeheader()
    for i in range(0, len(lines), batch_size):
        # if i>200:
        #     break;
        print(i)
        batch = lines[i:i+batch_size]
        # Skip empty batches
        if not any(line.strip() for line in batch):
            continue
        # Join lines into a single text
        batch_text = '\n'.join(batch)
        # Extract entities using SpaCy 'en_ner_bc5cdr_md'
        # ans1,ans2=test_beam (nlp, batch_text)
        # ans1,ans2 = zip(*sorted(zip(ans1,ans2)))
        
        doc_ner_bc5cdr_md = nlp_ner_bc5cdr_md(batch_text)
        for ent in doc_ner_bc5cdr_md.ents:
            entities_ner_bc5cdr_md.append((ent.text, ent.label_))
        all_entities_ner_bc5cdr_md.extend(entities_ner_bc5cdr_md)
        
        
        # Write entities to CSV
        for entity in entities_ner_bc5cdr_md:
            temp1=nlp.vocab[entity[0]]
            temp2=nlp.vocab[entity[1]]
            ans=temp1.similarity(temp2)
            csv_writer_ner_bc5cdr_md.writerow({'Text': entity[0], 'Label': entity[1], 'Score': ans})
            
            
# Print the extracted entities to the screen
print("Entities from 'en_ner_bc5cdr_md':", all_entities_ner_bc5cdr_md)