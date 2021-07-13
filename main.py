# Author: Harun Sheikhali
# Date: Wed June 30th
# Description: Simple python script to conver CSV to JSON
from zendesk_api.api import ZendeskApiHandler
import pandas as pd
import json


def make_json(csv_file_path, json_file_path='./'):
    '''
    function that will convert a CSV to JSON
    takes the file paths as args
    param: csv_file_path -> path to the actual csv file
    param: json_file_path -> path to where you want the json file to be created
    default is the root directory
    '''

    # use pandas to create csv
    data_file = pd.read_csv(csv_file_path)
    # use pandas to convert it to a json file
    data_file.to_json('./badi-example.json')


def post_to_zendesk():
    # read json file
    json_file = open('./badi-example.json')
    data = json.load(json_file)

    for i in data:
        print(data[i])

    json_file.close()

    # Initialize the API handler
    zendesk_api_hander = ZendeskApiHandler('', credentials={})

    # create ticket in zendesk
    # zendesk_api_hander.create_ticket(
    #     assignee='', priority='', subject='', body='')


if __name__ == "__main__":
    # make json
    # make_json(csv_file_path=r'./badi-example.csv')
    post_to_zendesk()
