import json
import os

class Case(dict):
    def __init__(self, person_id, case_number, balance, birth_year, location, violation_type, charges):
        self['person_id'] = person_id
        self['case_number'] = case_number
        self['balance'] = balance
        self['birth_year'] = birth_year
        self['location'] = location
        self['violation_type'] = violation_type
        self['charges'] = charges

class Charge(dict):
    def __init__(self, violation_type, eligibility, expunged, convicted):
        self['violation_type'] = violation_type
        self['eligibility'] = eligibility
        self['expunged'] = expunged
        self['convicted'] = convicted


def parse_data():
    data_path = os.path.join(os.getcwd(), 'records_data')

    data = []

    for dataFile in os.listdir(data_path):
        with open(os.path.join(data_path, dataFile), 'r') as f:
            data.append(json.load(f))

    for d in data:
        if(len(d['cases'])) == 0:
            # If file contains no data, skip to next file
            continue










if __name__ == '__main__':
    parse_data()