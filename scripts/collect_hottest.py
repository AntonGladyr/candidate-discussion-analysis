import requests
import json
import argparse
import datetime
import os
import os.path as osp


def load_posts(subreddit: str, num_of_posts: int = 1000):
    # Reddit posts json output
    # Example: https://www.reddit.com/r/AskReddit+memes/new.json?limit=100
    urltemplate = (
        "https://www.reddit.com/r/{subreddit}/hot.json?limit={limit}&count={count}&after={after}"
    )

    # User-Agent to use for fetch
    useragent = "Reddit-Collect 84cd488d"

    count = 0
    limit = 100
    after = ''

    posts = []

    while count < num_of_posts:
        # Generate URL
        url = urltemplate.format(
            subreddit=subreddit, limit=limit, count=count, after=after
        )
        resp = requests.get(url, headers={"User-Agent": useragent}).json()
        posts.extend(resp["data"]["children"])
        after = resp["data"]["after"]
        count = count + resp["data"]["dist"]

        if count + limit > num_of_posts:
            limit = num_of_posts - count

    return posts


def main():

    # Parse arguments
    argparse_root = argparse.ArgumentParser(description = "Collect Subreddits' Posts")
    argparse_root.add_argument(
        "-r",
        "--subreddits",
        help="List of subreddits to fetch",
        nargs='+',
        required=True,
    )
    argparse_root.add_argument(
        "-o", "--output_dir", help="Output directory", required=True
    )
    argparse_root.add_argument(
        "-c",
        "--count",
        help="Count of posts to fetch (default 1000)",
        type=int,
        default=1000,
    )
    args = argparse_root.parse_args()

    if not osp.isdir(args.output_dir):
        print('The directory path specified does not exist')
        exit()

    for subreddit in args.subreddits:
        # load posts
        posts = load_posts(subreddit, args.count)
        
        # create subdirectory for the subreddit
        subreddit_dir = osp.join(args.output_dir, subreddit)

        if not osp.exists(subreddit_dir):
            os.makedirs(subreddit_dir)
        
        # build file name
        dt_utc = datetime.datetime.now(datetime.timezone.utc)
        subreddit_output = osp.join(
                subreddit_dir,
                f"{subreddit}_hottest_{dt_utc.strftime('%Y-%m-%dT%H:%M:%S%z')}.json")

        # Load and save posts
        with open(subreddit_output, "w") as f:
            #f.write(f"{json.dumps(posts)}")
            f.write(
                '[' +
                ',\n'.join(json.dumps(post['data']) for post in posts) +
                ']\n'
            )
            #for post in posts:
            #    f.write(f"{json.dumps(post['data'])}\n")


if __name__ == "__main__":
    main()
