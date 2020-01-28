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
                row['rate_area_tuple'] = (row['state'], row['rate_area'])
                plan_data.append((row['rate'], row['rate_area_tuple']))
        return plan_data


def find_zips_in_multiple_rate_areas(zip_data):
    dupes = list()
    import pdb
    pdb.set_trace()
    for i, zip in enumerate(zip_data):
        compare = zip_data[i]['zipcode'], zip_data[i]['rate_area_tuple']

        compare1 = zip_data[i+1]['zipcode'], zip_data[i+1]['rate_area_tuple']
        import pdb
        pdb.set_trace()
        print(compare, compare1)

    # [zip for index, zip in enumerate(
    #     zip_data) if zip['rate_area_tuple'] not in zip_data[index + 1:]]
    # zip_data[0]['rate_area_tuple'] == zip_data[1]['rate_area_tuple']


zips_to_query = process_query()
zip_data = load_zips()
silver_plan_data = load_plans()
dupes = find_zips_in_multiple_rate_areas(zip_data)
