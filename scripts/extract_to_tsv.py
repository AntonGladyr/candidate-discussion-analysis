import os
import argparse
import json
import random


def main():
    # Parse arguments
    argparse_root = argparse.ArgumentParser(description="Extract posts from files")
    
    argparse_root.add_argument(
            '-i',
            '--input',
            help='List of input files',
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
            '-n',
            '--num_posts_to_output',
            help='Number of posts to output',
            type=int,
            required=True
    )

    args = argparse_root.parse_args()
     
    # check if the input json files exist
    for json_file in args.input:
        json_file_exists = os.path.isfile(json_file)
    
        if not json_file_exists:
            print(f"json {json_file} file does not exist")
            exit()
    
    posts_list = []
    # Load posts from files
    for json_file in args.input:
        with open(json_file) as f: 
            posts_list: List[dict] = json.loads(f.read()) 
            posts_list.extend(posts_list)    
   
    # Delete duplicates from posts list 
    posts = {}
    for post in posts_list: 
        if post['name'] not in posts:
            posts[post['name']] = {
                    'name': post['name'],
                    'title': post['title'],
                    'subreddit': post['subreddit']
            }

    posts = list(posts.values()) 
    
    # If after deleting duplicates
    # there are less posts than num_posts_to_output
    if len(posts) < args.num_posts_to_output:
        # add duplicates
        num_posts_to_add = args.num_posts_to_output - len(posts)
        posts_to_add = random.sample(posts_list, num_posts_to_add)
        posts.extend(posts_to_add)
        random.shuffle(posts)
        print(f'Duplicates added: {len(posts_to_add)}')

    # If there are more posts than num_posts_to_output,
    # randomly select num_posts_to_output of them
    if len(posts) > args.num_posts_to_output:
        posts = random.sample(posts, args.num_posts_to_output)

    print(f'Dataset length: {len(posts)}')

    # Split the path in head and tail pair
    head_tail = os.path.split(args.output)
    dir_path = head_tail[0]

    if dir_path and not os.path.exists(dir_path):
        os.makedirs(dir_path)
 
    with open(args.output, "w") as f:
        f.write(f'name\ttitle\tsubreddit\ttopic\n')
        for post in posts:
            f.write(f'{post["name"]}\t{post["title"]}\t{post["subreddit"]}\t\n')


if __name__ == "__main__":
    main()
