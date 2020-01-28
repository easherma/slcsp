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


def load_zips():
    with open('./data/zips.csv', 'r', newline='') as file:
        reader = csv.DictReader(file)
        zip_data = list()
        for row in reader:
            if row['zipcode'] in zips_to_query:
                row['rate_area_tuple'] = (row['state'], row['rate_area'])
                zip_data.append(row)
        return zip_data


def find_zips_in_multiple_rate_areas(zip_data):
    pass


zips_to_query = process_query()
zip_data = load_zips()
pdb.set_trace()
