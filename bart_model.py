from transformers import BartForConditionalGeneration, BartTokenizer
from typing import List

def old_summarization_pipeline(text: List[str]) -> List[str]:
    tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')
    model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')
    input_ids = tokenizer.batch_encode_plus(text, return_tensors='pt', max_length=1024)['input_ids']
    summary_ids = model.generate(input_ids)
    summaries = [tokenizer.decode(s) for s in summary_ids]
    return summaries
