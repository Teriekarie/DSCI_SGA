# program to import the file
# importing a csv file

# import csv

# with open('raw data1.csv', newline='') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     for row in csv_reader:
#         print(','.join(row))

# with open("cool_document.txt") as cool_doc:
#     for line in cool_doc.readlines():
#         print(line);

# created_doc = open('created_file.txt', 'a')
# open a line
# created_doc.write('Latest line')

# created_doc.close()


# writing a csv file
big_list = [
    {'name': 'Joy Okum', 'id': 485690, 'sex': 'Female'},
    {'name': 'Baker Jones', 'id': 445939, 'sex': 'male'},
    {'name': 'Fay Lanes', 'id': 485879, 'sex': 'Female'},
    {'name': 'Peyton Mark', 'id': 481647, 'sex': 'Female'}
]

import csv

with open('output.csv', 'b') as output_csv:
    fields = ['name', 'id', 'sex']
    output_writer = csv.DictWriter(output_csv, fieldnames=fields)
    output_writer.writeheader()
    
    for item in big_list:
        output_writer.writerow(item)