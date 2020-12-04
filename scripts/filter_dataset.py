import os.path as osp
import argparse
import numpy as np
import re


POST_TITLE_INDEX = 1

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

    tweets_dataset = tweets_dataset[tweets_dataset[:, TWEET_LANGUAGE_INDEX] == ENGLISH_LANG]

    trump_mention_tweets = np.array([bool(re.search(r'\b\W*Trump\W*\b', val)) for val in tweets_dataset[:, TWEET_CONTENT_INDEX]])
    trump_mention_col = np.array(np.where(trump_mention_tweets == True, 'T', 'F'))
    trump_mention_col = np.reshape(trump_mention_col, (trump_mention_col.shape[0], 1))
   
    return np.array(np.hstack((posts_dataset, trump_mention_col)))


def main():
    # Parse arguments
    argparse_root = argparse.ArgumentParser(description="Filter dataset")

    argparse_root.add_argument(
            '-i',
            '--input',
            help='Input file',
            nargs='+',
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

    # check if the dataset file exists
    fileExists = osp.isfile(args.input)
    if fileExists == False:
        print(f'File \'{args.input}\' does not exist')
        exit()




if __name__ == '__main__':
    main()
