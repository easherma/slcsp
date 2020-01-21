import pdb
import sys
import pandas as pd


def load_data():
    """
    loads provided data into pandas dataframes:
    >>> plans_by_area, areas_by_zip, second_lowest_plan = load_data()
    >>> plans_by_area.columns
    Index(['state', 'metal_level', 'rate', 'rate_area'], dtype='object')
    >>> areas_by_zip.columns
    Index(['zipcode', 'state', 'county_code', 'name', 'rate_area'], dtype='object')
    >>> second_lowest_plan.columns
    Index(['zipcode', 'rate'], dtype='object')
    """
    plans_by_area = pd.read_csv(
        './data/plans.csv', dtype={'rate_area': 'str'}, index_col='plan_id')
    areas_by_zip = pd.read_csv(
        './data/zips.csv', dtype={'zipcode': 'str', 'rate_area': 'str', 'county_code': 'str'})
    second_lowest_plan = pd.read_csv(
        './data/slcsp.csv', dtype={'zipcode': 'str', 'rate_area': 'str'})
    return plans_by_area, areas_by_zip, second_lowest_plan


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
    benchmark_plans = silver_plans.groupby(by=['state', 'rate_area'])[
        'rate'].nsmallest(2).drop_duplicates()
    return benchmark_plans


def ambigious_zip_cases():
    # get a set (unique values) of rate areas by zip code
    rates = areas_by_zip.groupby(['zipcode'])['rate_area'].apply(set)
    ambigious_cases = rates[rates.str.len() > 1]
    return ambigious_cases


def link_plans_to_zips(*args):
    linked_plans_zips = pd.merge(
        areas_by_zip, return_benchmark_plans(),
        how='left', left_on=['state', 'rate_area'],
        right_on=['state', 'rate_area'])
    return linked_plans_zips


def merge(*args):
    """
    big ol mess here
    """
    link_output_to_zip_plans = pd.merge(
        second_lowest_plan,
        link_plans_to_zips(),
        how='left',
        on='zipcode'
    )
    values = link_output_to_zip_plans.groupby(['zipcode'])['rate_y'].apply(set)
    filtered_values = values[values.str.len() == 1]
    merged = pd.merge(
        second_lowest_plan, filtered_values, how='left',
        left_on='zipcode', right_on=filtered_values.index)

    # ugly cleanup
    merged['rate'] = merged['rate_y']
    merged.set_index('zipcode')
    del merged['rate_y']

    return merged


def output(data):
    data.to_csv(sys.stdout)


if __name__ == '__main__':
    plans_by_area, areas_by_zip, second_lowest_plan = load_data()
    merged = merge()
    output(merged)
