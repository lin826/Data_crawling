import json

input_file = 'user_data_survey.json'
output_file = 'clean_'+input_file
LIST = list()

with open(output_file, 'w') as outfile:
    with open(input_file) as infile:
        for data in infile.readline():
            outfile.write(data.replace('},{','}{'))
            # data = json.load(json_data)
            # for d in data:
            #     for p in d['pictures']:
            #         tags = list()
            #         for t in p['hashtags']:
            #             for item in t.split('#'):
            #                 tags.append(item)
            #         p['hashtags'] = tags
            #     json.dump(d, outfile)
