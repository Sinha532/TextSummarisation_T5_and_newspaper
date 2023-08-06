import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration, T5Config

model = T5ForConditionalGeneration.from_pretrained('t5-small')
tokenizer = T5Tokenizer.from_pretrained('t5-small')
device = torch.device('cpu')
    
def declare_text(text):
    preprocessed_text = text.strip().replace('\n','')
    t5_input_text = 'summarize: ' + preprocessed_text

    return t5_input_text

def summarize(input):
    tokenized_text = tokenizer.encode(input, return_tensors='pt', truncation=True,max_length=len(input)).to(device)
    summary_ids= model.generate(tokenized_text, min_length=30, max_length=120)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    return summary





