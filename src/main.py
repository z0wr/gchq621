import json
import time

import requests


POSTS_URL = "https://e621.net/posts.json?limit=10&tags=order:random%20~scat%20~hyper%20~vore"
HEADERS = {
    "user-agent": "gchq621/0.1.0 (by @z0wr on discord)"
}


def get_post_urls() -> set:
    response = requests.get(POSTS_URL, headers=HEADERS)

    response.raise_for_status()

    raw = response.text
    posts = json.loads(raw)["posts"]
    
    urls = set()

    for post in posts:
        image = post["file"]
        url = image["url"]

        if url is not None:
            urls.add(url)

    print(posts)

    return urls


def main():
    while True:
        post_urls = get_post_urls()

        for url in post_urls:
            response = requests.get(url, headers=HEADERS)
            response.raise_for_status()
            
            time.sleep(60)



if __name__ == '__main__':
    main()