import pdb
import csv
import sys


def process_query():
    with open('./data/slcsp.csv', 'r', newline='') as output:
        reader = csv.DictReader(output)
        output_writer = csv.DictWriter(sys.stdout, fieldnames=reader.fieldnames)
        output_writer.writeheader()
        zips = []
        for row in reader:
            zips.append(row['zipcode'])
            output_writer.writerow(row)
        return zips


def load_file(filepath):
    with open(filepath, 'r', newline='') as file:
        reader = csv.DictReader(file)
        return reader


zips_to_query = process_query()
