from nltk.corpus import stopwords
def return_words(summary):
    split_sentences = summary.split()
    filtered_words = [word for word in split_sentences if word not in stopwords.words('english')]
    return filtered_words
