import math
import sys
import pandas as pd
import itertools
import re
from collections import Counter

def tokenize(tweet):
    return [x.lower() for x in re.split("[^a-zA-Z']",tweet)]

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

    for tweet, coding in zip(df["title"], df["topic"]):
        tokenized_tweet = tokenize(tweet)
        for tok in tokenized_tweet:
            counters[coding].update((tok, 1))

    counters_to_tfidf(list(counters.values()))

    for k, c in counters.items():
        print("\n==================")
        print(k)
        for word, tfidf in c.most_common(10):
            print(word, tfidf)

if __name__ == "__main__":
    main()
