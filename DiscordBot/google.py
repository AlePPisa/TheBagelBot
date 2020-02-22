#! python3.6


__author__ = 'stephy'

import requests
from googleapiclient.discovery import build
from dotenv import load_dotenv
import os
import random


load_dotenv()
my_cse_id = os.getenv("CSE_ID")
dev_key = os.getenv("DEV_TOKEN")

SEARCH = 10
START = random.randint(1, 10)*10


def google_search(search_term, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=dev_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']


def get_random_img(keyword: str) -> str:
    results = google_search(keyword, my_cse_id,
                            num=SEARCH, searchType='image', start=START)

    res = []
    for result in results:
        try:
            img = result.get('link')
            if img:
                res.append(img)
        except Exception as e:
            print("None shit")
    return random.choice(res)


if __name__ == "__main__":
    print(get_random_img("hannibal lecter"))
