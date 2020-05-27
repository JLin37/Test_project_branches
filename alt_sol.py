import os
import csv
import pprint

udemy_csv = "../Resources/web_starter.csv"

data_list = []
# with open(udemy_csv, encoding='utf-8') as csvfile:
with open(udemy_csv, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        data_dict = {}
        # Add title
        data_dict['Title'] = row[1]

        # Add price
        data_dict['Course Price'] = row[4]

        # Add number of subscribers
        data_dict['Subscribers'] = row[5]

        # Add amount of reviews
        data_dict["Reviews Left"] = row[6]

        # Determine percent of review left to 2 decimal places
        percent = round(int(row[6]) / int(row[5]), 2)
        data_dict['Percent of Reviews'] = percent

        # Get length of the course to just a number
        new_length = row[9].split(" ")
        data_dict['Length of Course'] = float(new_length[0])

        data_list.append(data_dict)

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(data_list[:10])
# Set variable for output file
output_file = os.path.join("web_final2.csv")

csvheader = list(data_dict.keys())
# print(csvheader)
#  Open the output file
with open(output_file, "w", newline='') as datafile:
    writer = csv.DictWriter(datafile, csvheader)
    writer.writeheader()
    writer.writerows(data_list)