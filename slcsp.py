import csv
import sys


def process_query():
    with open('./data/slcsp.csv', 'r', newline='') as output:
        reader = csv.DictReader(output)
        output_writer = csv.DictWriter(sys.stdout, fieldnames=reader.fieldnames)
        output_writer.writeheader()
        for row in reader:
            output_writer.writerow(row)


def load_file(filepath):
    with open(filepath, 'r', newline='') as file:
        reader = csv.DictReader(file)
        return reader


process_query()
