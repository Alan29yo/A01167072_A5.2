"""
Python program to compute the total cost for all
sales included in the input sales.json file.
"""

import sys
import time as t
import json


if __name__ == "__main__":
    start = t.time()
    FILEPATH_1 = sys.argv[1]
    FILEPATH_2 = sys.argv[2]
    REL_PATH = "../data/"

    with open(REL_PATH + FILEPATH_1, "r", encoding="utf-8") as f1:
        prod_list = json.load(f1)

    """
        for obj in prod_list:
            print(obj)
        print("\n\n")
    """

    with open(REL_PATH + FILEPATH_2, "r", encoding="utf-8") as f2:
        sales = json.load(f2)

        for obj in sales:
            print(obj)
        print("\n\n")

    prod_catalogue = {}
    for prod in prod_list:
        prod_catalogue[prod['title']] = float(prod['price'])

    total_cost = float(0)
    for sale in sales:
        if sale['Product'] in prod_catalogue:
            total_cost += prod_catalogue[sale['Product']] \
                          * int(sale['Quantity'])
        else:
            print("The product", sale['Product'],
                  "couldn't be found in the catalogue")
    print("Total cost is: $", round(total_cost, 2))

    end = t.time()
    exec_time = (end-start) * 1000
    print("\n\nThe elapsed execution time is :", exec_time, "ms")

    with open(REL_PATH + "SalesResults.txt", "w", encoding="utf-8") as f3:
        f3.write("Total cost is: $" + str(round(total_cost, 2)) + "\n")
        f3.write("\nThe elapsed execution time is :" + str(exec_time) + " ms")
