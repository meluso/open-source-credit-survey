# -*- coding: utf-8 -*-

import csv

def load_csv(file_name):
    """
    Loads a CSV file into a list of lists.

    Args:
        file_name (str): The name of the CSV file to load.

    Returns:
        A list of lists containing the data from the CSV file.
    """

    with open(file_name, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        data = []
        for row in reader:
            data.append(row)
    return data
