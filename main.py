# Author: Harun Sheikhali
# Date: Wed June 30th
# Description: Simple python script to conver CSV to JSON
from zendesk_api.api import ZendeskApiHandler
import csv
import json


def make_json(csv_file_path, json_file_path='./'):
    """
    function that will convert a CSV to JSON
    takes the file paths as args
    param: csv_file_path -> path to the actual csv file
    param: json_file_path -> path to where you want the json file to be created
    default is the root directory
    """
    data = {"tickets": []}  # this is the dictionary that we want to use for our data

    with open(csv_file_path, encoding='utf-8-sig')as csv_file:
        csv_reader = csv.DictReader(csv_file)

        # Convert each row into a dictionary
        for rows in csv_reader:
            # Assuming a column named 'No' to be the primary key
            payload = {
                "requester_id": rows['Assignee'],
                "assignee_id": rows['Assignee'],
                "status": rows['status'],
                "type": rows['type'],
                "subject": rows['subject'],
                "brand_id": rows['brand_id'],
                "priority": rows['priority'],
                "group_id": rows['group_id'],
                "organization": rows['organization_id'],
                "comment": {
                    "body": rows['description']
                },
                "custom_fields": [
                    {"id": rows['custom_field'], "value": ''}
                ]
            }

            data['tickets'].append(payload)

    with open(json_file_path, 'w', encoding='utf-8')as json_file:
        json_file.write(json.dumps(data, indent=4))


if __name__ == "__main__":
    # make json
    make_json(csv_file_path=r'./badi-example.csv', json_file_path='./badi-example.json')
