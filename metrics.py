import spacy
from textstat.textstat import textstatistics, legacy_round
import textstat

def split_sentences(text):
	set = spacy.load('en')
	sent = set(text)
	return sent.sents

def num_sentences(text):
	set = spacy.load('en')
	sent = set(text)
	return len(list(sent.sents))

def num_words(text):
    num_words = 0
    sentence_list = split_sentences(text)
    for sentence in sentence_list:
        for word in sentence:
            num_words += 1
    return num_words

def avg_sent_length(text):
	word_num = num_words(text)
	nums_sentences = num_sentences(text)
	avg_sent_length = float(word_num / nums_sentences)
	return avg_sent_length

def syllables_count(word):
	return textstatistics().syllable_count(str(word))

def total_syllables(text):
    num_syllables = 0
    sentence_list = split_sentences(text)
    for sentence in sentence_list:
        for word in sentence:
            num_syllables += syllables_count(word)
    return num_syllables



def avg_syllables_per_word(text):
	syllables_counts = syllables_count(text)
	nums_words = num_words(text)
	avg_syllables_per_word = float(syllables_counts) / float(nums_words)
	return (avg_syllables_per_word * 100) / 100

def hard_words(text):
    hard_words = []
    my_sents = split_sentences(text)

    for sentence in my_sents:
        for word in sentence:
            hard_words += str(word)
    hard_words_set = set()
    for hard_word in hard_words:
        num_syllables = syllables_count(hard_word)
        if hard_word not in textstat.textstat._textstatistics__get_lang_easy_words() and num_syllables >= 2:
            hard_words_set.add(hard_word)
    return len(hard_words_set)


def fre(text):
	return ((206.835 - (1.015 * float(num_words(text)/num_sentences(text))) -
		(84.6 * float(total_syllables(text)/num_words(text)))))

def gf(text):
	return (0.4 * (float(num_words(text)/num_sentences(text)) +
		(100 * (hard_words(text) / num_words(text)))))


text = ""

print("Flesch Reading Ease Index: " + str(fre(text)))
print("Gunning Fog Index: " + str(gf(text)))
