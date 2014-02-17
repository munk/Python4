import pandas as pd
from numpy.random import choice


boros = {'manhattan': 1,
         'bronx': 2,
         'brooklyn': 3,
         'queens': 4,
         'staten': 5}


def _filter_latest_grades_(data):
    camis_groups = data.groupby('CAMIS', as_index=False).first()
    camis_groups.dropna(subset=['CURRENTGRADE'], how='all')
    return camis_groups


def _sample_zipcodes_(data, count):
    def sample(data, count):
        rows = choice(data.index.values, count)
        sampled = data.ix[rows]
        return sampled
    sampled = [(int(name), sample(d, count)) for name, d in data]
    return sampled


def inspection_data(boro, samplesize):
    webextract = 'data/WebExtract.txt'
    data = pd.read_csv(webextract)
    key = boros[boro]
    boro_data = data.groupby('BORO').get_group(key)
    filtered = _filter_latest_grades_(boro_data)
    zipcodes = filtered.groupby('ZIPCODE')
    sampled = _sample_zipcodes_(zipcodes, samplesize)
    return sampled

inspection_data('manhattan', 10)
