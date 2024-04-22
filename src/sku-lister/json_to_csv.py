
import json
import csv

input = './data/md_out.json'

with open(input) as f:
    data = json.load(f)


data_file = open(input.replace(".json", ".csv"), 'w') 
csv_writer = csv.writer(data_file)
 
count = 0
for offer in data:
    if count == 0:
        headers = ["offer"]
        regions = data[count]['regionalSKUs']
        for region in regions:
            headers.append(region['region'])
        csv_writer.writerow(headers)

    row = [data[count]['offer']]
    skus = data[count]['regionalSKUs']
    for sku in skus:
        row.append(sku['SKU'])

    csv_writer.writerow(row)        
    count += 1

 
data_file.close()




