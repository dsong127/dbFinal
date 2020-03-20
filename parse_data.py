import json
import os
from datetime import datetime


def parse_data():
    data_path = os.path.join(os.getcwd(), 'records_data')

    jsonFiles= []
    parsed_cases = []


    for dataFile in os.listdir(data_path):
        with open(os.path.join(data_path, dataFile), 'r') as f:
            jsonFiles.append(json.load(f))


    for i, record in enumerate(jsonFiles):

        if(len(record['cases'])) == 0:
            # If file contains no data, skip to next file
            continue

        now = datetime.now()
        # print('file {}'.format(i))

        for i, case in enumerate(record['cases']):
            # print('case {}'.format(i))

            person_id = case['name']
            age = now.year - case['birth_year']


            balance = case['balance_due']
            case_number = case['case_number']
            location = case['location']
            violation_type = case['violation_type']



            charges = []
            for i, charge in enumerate(case['charges']):
                # print('charge {}'.format(i))
                try:
                    e1= charge['expungement_result']
                    e2 = e1['type_eligibility']
                    eligibility = e2['status']
                    convic= charge['disposition']

                    convicted = convic['status']

                    charge = {'eligibility': eligibility, 'convicted': convicted}
                    charges.append(charge)
                except:
                    continue

            case = {'person_id': person_id, 'age': age, 'case_number': case_number,
                    'balance': balance, 'location': location, 'violation_type': violation_type,
                    'charges': charges}

            parsed_cases.append(case)
            # print(case)

            # print('---------------------------')

    return parsed_cases



if __name__ == '__main__':
    parse_data()