#!/bin/python3

import requests
from typing import List


global author_endpoint
author_endpoint = (
    "https://jsonmock.hackerrank.com"
    + "/api/articles?author={author_name}&page={page}"
)


def getArticleTitles(author: str) -> List[str]:
    """
    Given an author's name, returns the list of all
    the titles of articles that author has written.

    Parameters
    ----------
    author: str
        The author to query's last name in lower case.

    Returns
    -------
    titles: List[str]
        List of all the titles of articles written by the author.
    """
    titles = []
    total_pages = requests.get(
        author_endpoint.format(author_name=author, page=0)
    ).json()["total_pages"]
    for i in range(total_pages):
        page = requests.get(
            author_endpoint.format(author_name=author, page=i + 1)
        )
        for line in page.json()["data"]:
            if line["title"]:
                titles.append(line["title"])
            elif line["story_title"]:
                titles.append(line["story_title"])
    return titles


def test_getArticleTitles():
    """Test for getArticleTitles function."""
    assert getArticleTitles(author="epaga") == [
        "A Message to Our Customers",
        (
            "“Was isolated from 1999 to 2006 with a 486. "
            "Built my own late 80s OS”"
        ),
        "Apple’s declining software quality",
    ]
    assert getArticleTitles(author="saintamh") == [
        "Google Is Eating Our Mail",
        "Why I’m Suing the US Government",
    ]


test_getArticleTitles()
author = input()
results = getArticleTitles(author)
for result in results:
    print(result)
