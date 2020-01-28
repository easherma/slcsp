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

                zip_data.append((row['zipcode'], row['rate_area_tuple']))
        return zip_data


def load_plans():
    with open('./data/plans.csv', 'r', newline='') as file:
        reader = csv.DictReader(file)
        plan_data = list()
        for row in reader:
            if row['metal_level'] == 'Silver':
                # TODO: second lowest
                row['rate_area_tuple'] = (row['state'], row['rate_area'])
                plan_data.append((row['rate'], row['rate_area_tuple']))
        return plan_data


def find_zips_in_multiple_rate_areas(zip_data):
    # list of tuples to remove
    zips_in_multiple_rate_areas = list()
    # for refrence, counts of occurence next to each tuple
    zip_counts = [[zip_data.count(zip), zip] for zip in zip_data]
    # filter to only test multple occurence tuples
    multiples = [zip for zip in zip_data if zip_data.count(zip) > 1]

    for test_case in multiples:
        test = [item for item in zip_data if item[0] == test_case[0]]
        test_set = set(test)
        if len(test_set) > 1:
            # this means a zip is in more than one rate area
            zips_in_multiple_rate_areas += test
    return zips_in_multiple_rate_areas


zips_to_query = process_query()
zip_data = load_zips()
silver_plan_data = load_plans()
dupes = find_zips_in_multiple_rate_areas(zip_data)
pdb.set_trace()
