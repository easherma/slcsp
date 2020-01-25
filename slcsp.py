import pdb
import sys
import pandas as pd


def load_data():
    """
    loads provided data into pandas dataframes:
    >>> plans_by_area, areas_by_zip, ouput = load_data()
    >>> plans_by_area.columns
    Index(['state', 'metal_level', 'rate', 'rate_area'], dtype='object')
    >>> areas_by_zip.columns
    Index(['zipcode', 'state', 'county_code', 'name', 'rate_area'], dtype='object')
    >>> ouput.columns
    Index(['zipcode', 'rate'], dtype='object')
    """
    plans_by_area = pd.read_csv(
        './data/plans.csv', dtype={'rate_area': 'str'}, index_col=['state', 'rate_area'])
    areas_by_zip = pd.read_csv('./data/zips.csv', dtype={
                               'zipcode': 'str', 'rate_area': 'str', 'county_code': 'str'}, index_col=['state', 'rate_area'])
    zips_for_query = pd.read_csv(
        './data/slcsp.csv', dtype={'zipcode': 'str', 'rate_area': 'str'})
    return plans_by_area, areas_by_zip, zips_for_query


def return_benchmark_plans():
    """
    just silver plans
    >>> len(plans_by_area)
    22240
    >>> len(silver_plans)
    8462
    >>> len(benchmark_plans)
    639
    """
    silver_plans = plans_by_area[plans_by_area['metal_level'] == 'Silver']
    silver_plans.groupby(silver_plans.index)['rate'].apply(list)
    rates = silver_plans.groupby(silver_plans.index)['rate'].apply(set)
    rates = rates.apply(sorted)
    benchmark_plans = rates.apply(pd.Series)[1]
    return benchmark_plans


def ambigious_zip_cases():
    # get a set (unique values) of rate areas by zip code
    rates_by_zip = areas_by_zip.groupby(['zipcode'])['rate_area'].apply(set)
    ambigious_cases = rates_by_zip[rates_by_zip.str.len() > 1]
    return ambigious_cases


def merge(*args):
    """
    big ol mess here
    """
    only_output_zips = areas_by_zip[areas_by_zip['zipcode'].isin(
        zips_for_query['zipcode'])]
    only_output_zips.index = only_output_zips.index.to_flat_index()
    zips_to_plans = pd.merge(only_output_zips, return_benchmark_plans(), left_index=True,
                             right_index=True, how='inner')

    return zips_to_plans


def output(data):
    data.to_csv(sys.stdout, index=False)


if __name__ == '__main__':
    plans_by_area, areas_by_zip, zips_for_query = load_data()
    merged = merge()
    merged = merged.drop_duplicates('zipcode', keep=False)
    results = zips_for_query.merge(merged, on='zipcode', how='left')
    results['rate'] = results[1]
    results = results[['zipcode', 'rate']]
    output(results)
