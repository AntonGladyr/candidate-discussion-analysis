import json
import argparse
import math

def tf_idf(data, ponyName, num, p):
    tf_idf = {}
    for word in data[ponyName].keys():
        tf = data[ponyName][word]
        df = 0
        if p :
            num = 0
            for names in data.keys():
                num = num +1
                if word in data[names].keys():
                    df = df+1
        else:
            for names in data.keys():
                if word in data[names].keys():
                    df = df + data[names][word]
        idf = math.log10(num/df)
        tf_idf[word] = tf*idf
    return tf_idf

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", action="store_true")
    parser.add_argument('inputFile',
                        help ='name of the JSON file in which clean dialogs were stored; should include the path... should be a .json file',
                        default = '../data/stdout.json')
    parser.add_argument('num_words')
    parser.add_argument('-o', '--outputFile',
                        help ='name of the JSON file in which you want to save your data; should include the path... should be a .json file',
                        default = '../data/tfidf.json')
    
    args = parser.parse_args()
    
    input_file = args.inputFile
    data = {}
    
    with open(input_file, 'r') as json_file:
        data=json.load(json_file)
  
    num = 0
    pony_tfidf = {}
    pony_tfidf_selected = {}
    for ponyName in data.keys():
        pony_tfidf[ponyName] = {}
        pony_tfidf_selected[ponyName] = []
        for word in data[ponyName].keys():
            num = num + data[ponyName][word]
            
            
    for ponyName in data.keys():
        pony_tfidf[ponyName] = tf_idf(data, ponyName, num, args.p)
        
    for name, words in pony_tfidf.items() :
        rankedWords = []
        for key, value in  words.items():
            rankedWords.append((value,key))
        rankedWords.sort(reverse = True)
        for count, word in rankedWords[:int(args.num_words)]:
            pony_tfidf_selected[name].append((word, count))
            
    with open(args.outputFile, 'w') as json_file:
        json.dump(pony_tfidf_selected, json_file)
        
if __name__ == '__main__':
    main()
           
    
    
    
        
    