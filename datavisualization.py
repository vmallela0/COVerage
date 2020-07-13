#something I found online:
import nltk
from urllib.request import urlopen
from bs4 import BeautifulSoup
url = "https://www.nature.com/articles/d41586-020-01449-8"
html = urlopen(url).read()

soup = BeautifulSoup(html)
#print(soup)
# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

#print(soup)

text = soup.get_text()
#print(text)
# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = 'n'.join(chunk for chunk in chunks if chunk)

#print(text)

#download and print the stop words for the English language
from nltk.corpus import stopwords
#nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
#print(stop_words)

#tokenise the data set
from nltk.tokenize import sent_tokenize, word_tokenize
#nltk.download('punkt')
words = word_tokenize(text)
#print(words)

# removes punctuation and numbers
wordsFiltered = [word.lower() for word in words if word.isalpha()]
#print(wordsFiltered)

# remove stop words from tokenised data set
filtered_words = [word for word in wordsFiltered if word not in stopwords.words('english')]
#print(filtered_words)

import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
#text = 'articles go here'
def generate_wordcloud(text): # optionally add: stopwords=STOPWORDS and change the arg below
    wordcloud = WordCloud(font_path='/Library/Fonts/Verdana.ttf',
        background_color='white',
        width=800, height=400,
        relative_scaling = 0.5,
         #stopwords = {'to','of'} # set or space-separated string
 ).generate(' '.join(filtered_words))
    fig = plt.figure(1, figsize=(8, 4))
    plt.axis('off')
    plt.imshow(wordcloud)
    plt.axis("off")
     ## Pick One:z
    plt.show()
     #plt.savefig("WordCloud.png")

generate_wordcloud(text)
