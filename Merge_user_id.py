import json
import csv

input_csv = 'mybirthday.csv'
input_json = 'result.json'
input_survey_csv = 'survey.csv'

output_csv = 'id.csv'


with open(output_csv, 'w') as outfile:
    fieldnames = ['username']
    with open(input_csv, 'rU') as file:
        file_content = csv.reader(file)
        spamwriter = csv.DictWriter(outfile, fieldnames=fieldnames, extrasaction='ignore')
        spamwriter.writeheader()
        for row in csv.reader(file, delimiter=','):
            spamwriter.writerow({fieldnames[0]:row[0]})
    with open(input_json) as json_data:
        data = json.load(json_data)
        for d in data:
            spamwriter.writerow({fieldnames[0]:d['id']})
    with open(input_survey_csv, 'rU') as csv_file:
        for row in csv.reader(csv_file, delimiter=','):
            spamwriter.writerow({fieldnames[0]:row[2]})
