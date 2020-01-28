import csv
import sys


def process_query():
    with open('./data/slcsp.csv', 'r', newline='') as output:
        reader = csv.reader(output)
        output_writer = csv.writer(sys.stdout)
        for row in reader:
            output_writer.writerow(row)


process_query()
