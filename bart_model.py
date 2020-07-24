from transformers import BartForConditionalGeneration, BartTokenizer
from typing import List

def old_summarization_pipeline(text: List[str]) -> List[str]:
    tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')
    model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')
    input_ids = tokenizer.batch_encode_plus(text, return_tensors='pt', max_length=1024)['input_ids']
    summary_ids = model.generate(input_ids)
    summaries = [tokenizer.decode(s) for s in summary_ids]
    return summaries
text = """
The Justice Department’s internal watchdog found that a federal prison in California, where nearly 1,000 inmates have tested positive for coronavirus, was slow to implement safety measures and lacked adequate staffing to confront the growing pandemic. At Federal Correctional Complex Lompoc, in Santa Barbara County, California, a nationwide order to restrict the movement of prison staff wasn’t fully implemented for more than two weeks because of a staff shortage — possibly allowing workers to bring the virus inside prison walls, a review released Thursday by the Justice Inspector General’s office found. Two staff members who showed up for work in late March with coronavirus symptoms made it past a weak screening process, and one inmate who had complained of coronavirus symptoms on March 22, wasn’t isolated or tested for days. The review of Lompoc represents the first official scrutiny of the federal prison system’s handling of coronavirus after months of dire warnings from advocates and politicians that more needed to be done to protect the vulnerable prison population. Ninety-eight federal inmates have died since the start of the pandemic, including four at the California prison. In April, as the number of positive inmate cases across the federal system jumped towards 500, the inspector general’s office announced it would begin a series of remote inspections of a selection of the Bureau of Prison’s 122 facilities. The watchdog office has since surveyed over 38,000 prison employees nationwide and conducted phone interviews with staffers as well as a review of documents and data at 16 sites. The report on Lompoc, as well as a second report on FCC Tuscon in Arizona, are the first to be released, with more expected in the coming months. In an interview with CNN in April, the director of the Bureau of Prisons called confronting the pandemic the most challenging situation the federal prison situation has been confronted with in decades.
"""
print(old_summarization_pipeline(text))
