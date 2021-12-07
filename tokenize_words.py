import sys
from sys import getsizeof

import matplotlib.pyplot as plt
import numpy
from sklearn.feature_extraction.text import CountVectorizer, ENGLISH_STOP_WORDS

file = open("scraped_text.txt", "r")
plain_text = file.read()
file.close()
print("Total number of characters: {}".format(len(plain_text)))
print("Memory usage for the text: {} MB!".format(getsizeof(plain_text) / (2 ** 20)))

stop_words_list = ENGLISH_STOP_WORDS.union(["like", "don", "just", "http", "https", "ve", "com", "going"])
vectorizer = CountVectorizer(stop_words=stop_words_list)
X = vectorizer.fit_transform([plain_text])
words_token = vectorizer.get_feature_names_out()
occurrence = X.toarray()[0]
numpy.set_printoptions(threshold=sys.maxsize)
# print(words_token)

max_indices = numpy.argpartition(occurrence, -20)[-20:]
max_tokens = words_token[max_indices]
max_occ = occurrence[max_indices]

plt.bar(max_tokens, max_occ)
plt.title("Top 20 frequent words")
plt.xlabel('Keyword')
plt.ylabel('Occurrences')
plt.xticks(
    rotation=45,
    horizontalalignment='right',
    fontweight='light',
    fontsize=9
)
plt.tight_layout()
plt.show()

