import os.path as osp
import argparse
import numpy as np
import pandas as pd
import re


POST_TITLE_INDEX = 1
POSTS_HEADER = ['name', 'title', 'subreddit', 'topic']

# keep rows which contain either "Trump" or "Biden"
def clean_data(posts_dataset, keywords) -> np.array:
    '''
    The string "Trump"/"Biden" is a word when
    (1) the "T"/"B" is capitalized and
    (2) it is not directly proceeded by an alphanumeric (number or letter) and
    (3) it is not directly followed by an alphanumeric. 
    '''
    
    '''
    \W* matches any non-word character (equal to [^a-zA-Z0-9_])
    \b a word boundary
    '''
    
    regex_keywords = ''
    for keyword in keywords:
        if keyword == keywords[0]:
            regex_keywords += f'{keyword}|{keyword.upper()}'
        else:
            regex_keywords += f'|{keyword}|{keyword.upper()}'

    #regexp = re.compile(fr'\b\W*{regex_keywords}\W*\b')

    regexp = fr'\b\W*{regex_keywords}\W*\b'
    #rows_to_keep = [bool(regexp.search(title)) for val in posts_dataset[:, POST_TITLE_INDEX]]
    #posts_dataset = posts_dataset[rows_to_keep]
    posts_dataset = posts_dataset[posts_dataset['title'].str.contains(regexp, case=True, regex=True)]
    return posts_dataset


        #tweets_dataset = tweets_dataset[tweets_dataset[:, TWEET_LANGUAGE_INDEX] == ENGLISH_LANG]

        #trump_mention_tweets = np.array([bool(re.search(r'\b\W*Trump\W*\b', val)) for val in tweets_dataset[:, TWEET_CONTENT_INDEX]])
        #trump_mention_col = np.array(np.where(trump_mention_tweets == True, 'T', 'F'))
        #trump_mention_col = np.reshape(trump_mention_col, (trump_mention_col.shape[0], 1))
   
    #return np.array(np.hstack((posts_dataset, trump_mention_col)))


def load_posts_df(dataset_path: str) -> pd.DataFrame: 
    # check if the given dataset file exists
    posts_file_exists = osp.isfile(dataset_path)
    if posts_file_exists == False:
        print(f'File \'{args.input}\' does not exist')
        exit()
    
    return pd.read_csv(dataset_path, delimiter='\t', skipinitialspace=True)


def main():
    # Parse arguments
    argparse_root = argparse.ArgumentParser(description="Filter dataset")

    argparse_root.add_argument(
            '-i',
            '--input',
            help='Input file', 
            required=True
    )

    argparse_root.add_argument(
            '-o',
            '--output',
            help='Output file',
            required=True
    )

    argparse_root.add_argument(
            '-k',
            '--keywords',
            nargs='+',
            help='Keep only posts that mention the keywords',
            default=[]
    )

    args = argparse_root.parse_args()

    df = load_posts_df(args.input)

    df = clean_data(df, args.keywords)

    # Split the path in head and tail pair
    head_tail = osp.split(args.output)
    dir_path = head_tail[0]

    if dir_path and not osp.exists(dir_path):
        os.makedirs(dir_path)

    pd.DataFrame(df).to_csv(
            args.output,
            sep="\t",
            index=False,
            header=POSTS_HEADER
    )


if __name__ == '__main__':
    main()
