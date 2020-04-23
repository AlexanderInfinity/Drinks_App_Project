import csv

def csv_load(file):
    temp_list = []
    try:
        with open(file,"r") as csv_file:
           rows = csv.reader(csv_file, quoting=csv.QUOTE_ALL, skipinitialspace=True)
           for row in rows:
                temp_list.append(row)
        return temp_list
    except Exception as error:
        print(f" error {error}")
        