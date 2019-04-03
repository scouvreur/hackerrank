#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    # This functions takes in meal_cost, tip_percent
    # and tax_percent and returns the total price rounded
    # to the nearest dollar
    return meal_cost * (1 + (tip_percent + tax_percent)/100)

if __name__ == '__main__':
    meal_cost = float(input())
    tip_percent = int(input())
    tax_percent = int(input())
    total_cost = solve(meal_cost, tip_percent, tax_percent)
    print(round(total_cost))
