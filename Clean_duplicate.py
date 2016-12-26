import csv

input_file = 'mybirthday.csv'
output_file = 'clean_'+input_file
LIST = list()

with open(input_file, 'rU') as file:
    file_content = csv.reader(file)
    with open(output_file, 'w') as csvfile:
        fieldnames = file_content.next()
        spamwriter = csv.DictWriter(csvfile, fieldnames=fieldnames, extrasaction='ignore')
        spamwriter.writeheader()
        for row in csv.reader(file, delimiter=','):
            if(row[0] not in LIST):
                LIST.append(row[0])
                spamwriter.writerow({fieldnames[0]:row[0],
    				fieldnames[1]:row[1],
    				fieldnames[2]:row[2],
    				fieldnames[3]:row[3]})
