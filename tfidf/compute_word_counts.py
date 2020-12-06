import pandas as pd
import json
import re
import argparse
from nltk.corpus import stopwords

def words(dialogs, stopwords):
    words = {}
    conservative = {}
    politics = {}
        
    for index, row in dialogs.iterrows():
        topic = row['topic']
        speech = row['title']
        sub = row['subreddit']
        speech = str(speech).strip()
        if topic not in words.keys():
            words[topic] = {}
            conservative[topic] = {}
            politics[topic] = {}
            
        words_split = re.split("[^a-zA-Z']", speech)
        for word in words_split:
            correct = word.lower()
            if correct == '' or correct in stopwords:
                continue
            else:
                words[topic][correct] = words[topic].get(correct,0)+1
                if sub == 'Conservative':
                    conservative[topic][correct] = conservative[topic].get(correct,0)+1
                if sub == 'politics':
                    politics[topic][correct] = politics[topic].get(correct,0)+1
            
    return words, conservative, politics

def words_cleanup(words):
    clean_words = {}
    for name, content in words.items():
        clean_words[name] = {}
        
    for name in words.keys():
        all_words = words[name]
        items = all_words.items()
        for word, occ in items:
            if occ < 5:
                continue
            else:
                clean_words[name][word] = occ
                
    return clean_words
    

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--OutputFile',
                        help ='name of the JSON file in which you want to save your data... should be a .json file',
                        default = '../data/stdout.json')
    parser.add_argument('inputFile',
                        help ='name of the dialog file, with the relative or absolute path specified... should be a .csv file',
                        default = '../data/clean_dialog.csv')
    
    args = parser.parse_args()
    
    dialog_file = args.inputFile
    outname = args.OutputFile
    stop_words = set(stopwords.words('english'))
    
    dialogs = pd.read_csv(dialog_file)
    Words, cons, pol = words(dialogs, stop_words)
    clean_words = words_cleanup(Words)
    clean_pol = words_cleanup(pol)
    clean_cons = words_cleanup(cons)
    with open(outname, 'w') as json_file:
        json.dump(clean_words, json_file)
        
    with open('conservative.json', 'w') as json_file:
        json.dump(clean_cons, json_file)
        
    with open('politics.json', 'w') as json_file:
        json.dump(clean_pol, json_file)

if __name__ == '__main__':
    main()
