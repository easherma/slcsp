# notes from the readme + puesdocode
from slcsp import *
import pytest

"""
Tests for Expected output

"The order of the rows in your answer as emitted on stdout must stay the same as how they
appeared in the original `slcsp.csv`."

The first row should be the column headers: `zipcode,rate`

The remaining lines should output unquoted values with two digits after the decimal
place of the rates, for example: `64148,245.20`.

def test_output():
    assert output_headers = input_headers
    assert output_zip_list = input_zip_list
    assert dataformat = <5 digit zipcode>, <float>


"It may not be possible to determine a SLCSP for every ZIP code given; for example,

if there is only one silver plan available,
there is no _second_ lowest cost plan.

Check for cases where a definitive answer cannot be found and leave those cells
blank in the output CSV (no quotes or zeroes or other text).""

def test_one_is_none():
    fixture = 40813, [245]
    return_second_lowest(fixture)
    assert output = `40813,`
"""


@pytest.fixture(scope='module')
def with_data():
    zips_to_query = process_query()
    zip_data = load_zips(zips_to_query)
    silver_plans = load_plans()
    dupes = find_zips_in_multiple_rate_areas(zip_data)
    no_ambigious_zips = [zip for zip in zip_data if zip not in dupes]
    assert len(dupes) == 32


def test_ouput(capsys):
    process_query()
    captured = capsys.readouterr()
    first_line = captured.out.split('\n')[0]
    fifth_zip = captured.out.split('\n')[5][:5]
    last_zip = captured.out.split('\n')[-2][:5]
    assert first_line == 'zipcode,rate\r'
    assert fifth_zip == '51012'
    assert last_zip == '31551'


def test_zip_in_more_than_one_rate_area(with_data):
    pass
    # import pdb
    # pdb.set_trace()
    #
    # # for refrence, counts of occurence next to each tuple
    # # zip_counts = [[zip_data.count(zip), zip] for zip in zip_data]
    # assert len(dupes) == 32
    # example = [item for item in zip_data if item[0] == '56097']
    # tests = [item for item in zip_data if item[0] == '56097']
    # tests1 = [item for item in zip_data if item[0] == '39845']
    # zip_counts = [(zip_data.count(zip), zip_data[zip]) for zip in zip_data]
    # pass


def test_plans_are_only_silver():
    # we filter out plans when loading, lets make sure none snuck in
    pass


"""
Additional information tests


"A rate area is a tuple of a state and a number, for
example, NY 1, IL 14.""
(note, this is not the original shape of the data, might be a documentation error?)

"A ZIP code can potentially be in more than one county.""

Ok, this is true, but not clear from instructions if that matters.

"If the county can not be
determined definitively by the ZIP code,
it may still be possible to determine
the rate area for that ZIP code."

This feels like misdirection

"A ZIP code can also be in more than one rate area.

In that case, the answer is ambiguous
and should be left blank."

Ok, we can test this and correct the output accordingly. Seems like an odd request though.

This feels a little ambiguous. What about a case like this?
areas_by_zip[areas_by_zip['zipcode']=='99350']
zipcode state  county_code       name  rate_area
99350    WA        53005     Benton          5
99350    WA        53039  Klickitat          3
99350    WA        53077     Yakima          5


"""
