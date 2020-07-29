import collections
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')


def taggify(text):
    # Store tags in array
    tags = []
    # Initialize stop words - words we don't want to be included
    stop_words = set(stopwords.words('english'))
    # Store words and associated count in dictionary
    wordcount = {}
    for word in text.lower().split():
        if (word not in stop_words):
            if (word not in wordcount):
                wordcount[word] = 1
            else:
                wordcount[word] += 1
    word_counter = collections.Counter(wordcount)
    for word, count in word_counter.most_common(3):
        tags.append(word)
    return tags