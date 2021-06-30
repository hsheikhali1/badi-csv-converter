## Author: Harun Sheikhali
## Date: Wed June 30th
## Description: Simple python script to conver CSV to JSON
import csv
import json



def make_json(csv_file_path, json_file_path = './'):
    '''
    function that will convert a CSV to JSON
    takes the file paths as args
    param: csv_file_path -> path to the actual csv file
    param: json_file_path -> path to where you want the json file to be created
    default is the root directory
    '''

    data = {}

    with open(csv_file_path, encoding='utf-8') as csv_f:
        csv_reader = csv.DictReader(csv_f)

        for rows in csv_reader:
            key = rows['No']
            data[key] = rows


    with open(json_file_path, 'w', encoding='utf-8') as json_f:
        json_f.write(json.dumps(data, indent=4))


if __name__ == "__main__":
    make_json(csv_file_path='./example_csv.csv')


