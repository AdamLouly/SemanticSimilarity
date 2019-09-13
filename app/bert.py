from pytorch_pretrained_bert import BertTokenizer,BertForMaskedLM
from pytorch_pretrained_bert import BertTokenizer, BertModel, BertForMaskedLM,BertForNextSentencePrediction
import torch
import math


def get_segments(indexed_tokens):
    segs=[]
    i=0
    id=0
    for case in indexed_tokens:
        if(case ==102):
            id = 1
        segs.append(id)
    return segs

# Load pre-trained model tokenizer (vocabulary)
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
# Load pre-trained model (weights)
model = BertForNextSentencePrediction.from_pretrained('bert-base-uncased')
model.eval()
bertMaskedLM = BertForMaskedLM.from_pretrained('bert-base-uncased')
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# Tokenized input
def NextSentenceScore(sentence1,sentence2):
    text = '[CLS] '+sentence1+' [SEP] '+sentence2+' [SEP]'
    tokenized_text = tokenizer.tokenize(text)

    # Convert token to vocabulary indices
    indexed_tokens = tokenizer.convert_tokens_to_ids(tokenized_text)
    # Define sentence A and B indices associated to 1st and 2nd sentences (see paper)
    segments_ids = get_segments(indexed_tokens)
    # Convert inputs to PyTorch tensors
    tokens_tensor = torch.tensor([indexed_tokens])
    segments_tensors = torch.tensor([segments_ids])

    # Predict is Next Sentence ?
    predictions = model(tokens_tensor, segments_tensors )
    return float('%.3f'%float(predictions[0][0]))

print(NextSentenceScore("I have a problem in java class with hibernate database mapping","a data base mapping problems using hibernate and java "))
print(NextSentenceScore("I have a problem in java class with hibernate database mapping","I have a problem using javascript in mongo db database"))