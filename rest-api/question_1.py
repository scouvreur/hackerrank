#!/bin/python3

import requests
import os

#
# Complete the 'getTotalGoals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING team
#  2. INTEGER year
#

home_endpoint = "https://jsonmock.hackerrank.com/api/football_matches?year={year}&team1={team}&page={page}"
away_endpoint = "https://jsonmock.hackerrank.com/api/football_matches?year={year}&team2={team}&page={page}"


def getTotalGoals(team, year):
    # Write your code here
    total_pages = requests.get(
        home_endpoint.format(year=year, team=team, page=0)
    ).json()["total_pages"]
    home_goals = 0
    for i in range(total_pages):
        response = requests.get(home_endpoint.format(year=year, team=team, page=i + 1))
        for line in response.json()["data"]:
            home_goals += int(line["team1goals"])

    total_pages = requests.get(
        away_endpoint.format(year=year, team=team, page=0)
    ).json()["total_pages"]
    away_goals = 0
    for i in range(total_pages):
        response = requests.get(away_endpoint.format(year=year, team=team, page=i + 1))
        for line in response.json()["data"]:
            away_goals += int(line["team2goals"])

    return home_goals + away_goals


def test_getTotalGoals():
    """Test for the getTotalGoals function."""
    assert getTotalGoals(year=2011, team="Barcelona") == 35
    assert getTotalGoals(year=2014, team="Chelsea") == 92


if __name__ == "__main__":
    test_getTotalGoals()
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    team = input()
    year = int(input().strip())
    result = getTotalGoals(team, year)
    fptr.write(str(result) + "\n")
    fptr.close()
