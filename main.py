#!/usr/bin/env python3
import psycopg2

from parse_data import parse_data
import json


def main():

    parsed_cases = parse_data()

    conn = None
    try:
        conn = psycopg2.connect(host="localhost",
                                database="expunge",
                                port='5432',
                                user="danielsong"
                                )

        cur = conn.cursor()

        added_list = []

        for parsed_case in parsed_cases:
            # if parsed_case['person_id'] not in added_list:
            #     cmd = "INSERT INTO person (person_id, age) VALUES ({}, {})".format("'"+parsed_case['person_id']+"'", parsed_case['age'])
            #     cur.execute(cmd)
            #     added_list.append(parsed_case['person_id'])

            ##
            # cmd = "INSERT INTO holds (person_id, case_number) VALUES ({}, {}) ON CONFLICT DO NOTHING".format("'" + parsed_case['person_id'] + "'", "'"+parsed_case['case_number']+"'")

            # if parsed_case['case_number'] not in added_list:
            #     cmd = "INSERT INTO cases(case_number, balance, location, violation_type) VALUES({}, {}, {}, {})"\
            #         .format("'"+parsed_case['case_number']+"'", parsed_case['balance'], "'"+parsed_case['location']+"'", "'"+parsed_case['violation_type']+"'")
            #     cur.execute(cmd)
            #     added_list.append(parsed_case['case_number'])
            for charge in parsed_case['charges']:
                cmd = "INSERT INTO charges(case_number, eligibility, convicted) VALUES({}, {}, {})".format("'"+parsed_case['case_number']+"'", "'"+charge['eligibility']+"'", "'"+charge['convicted']+"'")
                cur.execute(cmd)




        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    main()