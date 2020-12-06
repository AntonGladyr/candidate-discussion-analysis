import math
import sys
import pandas as pd
import itertools
import re
from collections import Counter
from nltk.corpus import stopwords


stop_words = set(stopwords.words('english'))

def preprocess(post): 
    # Converting to lowercase
    post = post.lower() 

    # remove all the special characters
    post = re.sub(r'\W', ' ', post)

    # remove all digits
    post = re.sub("^\d+\s|\s\d+\s|\s\d+$", " ", post)

    #remove single characters
    post = ' '.join([w for w in post.split() if len(w) > 1])
    
     # remove all spaces, tabs or newline characters
    post = re.sub(r'\s+', ' ', post)

    # delete stop words 
    tokenized_post = [w for w in post.split() if not w in stop_words]

    return ' '.join(tokenized_post)


def tokenize(post):
    return [x for x in re.split("[^a-zA-Z']", post)]

def counter_to_tf(counter):
    total = sum(counter.values())
    for k in counter: 
        counter[k] = float(counter[k]) / total 

def idf_from_counters(counters):
    allwords = set(itertools.chain(w for c in counters for w in c.keys())) 
    return {w: math.log(len(counters) / sum(1 if w in c else 0 for c in counters)) for w in allwords}

def counters_to_tfidf(counters):
    word_idf = idf_from_counters(counters)
    for c in counters:
        counter_to_tf(c)
        for word in c:
            c[word] *= word_idf[word]

def main():
    df = pd.read_csv(sys.stdin)
    all_codings = set(df["topic"])
    counters = {c: Counter() for c in all_codings}

    for post, coding in zip(df["title"], df["topic"]):
        post = preprocess(post)
        tokenized_post = tokenize(post)
        for tok in tokenized_post:
            counters[coding].update((tok, 1))

    counters_to_tfidf(list(counters.values()))

    for k, c in counters.items():
        print("\n==================")
        print(k)
        for word, tfidf in c.most_common(10):
            print(word, tfidf)

if __name__ == "__main__":
    main()
