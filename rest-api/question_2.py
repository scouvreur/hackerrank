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

comp_endpoint = (
    "https://jsonmock.hackerrank.com/api/football_competitions?name={name}&year={year}"
)
home_endpoint = "https://jsonmock.hackerrank.com/api/football_matches?competition={comp}&year={year}&team1={team}&page={page}"
away_endpoint = "https://jsonmock.hackerrank.com/api/football_matches?competition={comp}&year={year}&team2={team}&page={page}"


def getCompWinner(comp, year):
    winner = requests.get(comp_endpoint.format(name=comp, year=year)).json()["data"][0][
        "winner"
    ]
    return winner


def getTotalGoals(comp, team, year):
    # Write your code here
    total_pages = requests.get(
        home_endpoint.format(comp=comp, year=year, team=team, page=0)
    ).json()["total_pages"]
    home_goals = 0
    for i in range(total_pages):
        response = requests.get(
            home_endpoint.format(comp=comp, year=year, team=team, page=i + 1)
        )
        for line in response.json()["data"]:
            home_goals += int(line["team1goals"])

    total_pages = requests.get(
        away_endpoint.format(comp=comp, year=year, team=team, page=0)
    ).json()["total_pages"]
    away_goals = 0
    for i in range(total_pages):
        response = requests.get(
            away_endpoint.format(comp=comp, year=year, team=team, page=i + 1)
        )
        for line in response.json()["data"]:
            away_goals += int(line["team2goals"])

    return home_goals + away_goals


def getWinnerTotalGoals(comp, year):
    # Write your code here
    winner = getCompWinner(comp, year)
    return getTotalGoals(comp, winner, year)


def test_getCompWinner():
    """Test for the getCompWinner function."""
    assert getCompWinner(comp="UEFA Champions League", year=2011) == "Chelsea"
    assert getCompWinner(comp="UEFA Champions League", year=2012) == "Bayern Munich"
    assert getCompWinner(comp="La Liga", year=2011) == "Real Madrid"


def test_getTotalGoals():
    """Test for the getTotalGoals function."""
    assert getTotalGoals(comp="La Liga", year=2011, team="Real Madrid") == 121
    assert (
        getTotalGoals(comp="UEFA Champions League", year=2012, team="Real Madrid") == 26
    )


if __name__ == "__main__":
    test_getCompWinner()
    test_getTotalGoals()
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    competition = input()
    year = int(input().strip())
    result = getWinnerTotalGoals(competition, year)
    fptr.write(str(result) + "\n")
    fptr.close()
