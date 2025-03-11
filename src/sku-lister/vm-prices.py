import json
import jmespath
import csv

# Regions to find SKU numbers for
regions = ['sweden-central', 'europe-west', 'europe-north', 'germany-west-central', 'france-central']

# Get input.json as follows
# - https://azure.microsoft.com/en-us/pricing/calculator/ - start fresh
# - Add Virtual Machines to cost
# - Log in (bottom of the page)
# - F12 dev tools - Network tab - clean it up
# - Hit 'Display Part Numbers' button at bottom of the page
# - Find the 5-6 meg download - save as input.json

input = './data/vms_in.json'
output_json = './data/vm_prices_out.json'
output_csv = './data/vm_prices_out.csv'

# price files is a key value pair of region and json data of the contents of the file
price_files = {}

# loop over the regions and find the file forin the /data folder with the same name as the region + .json
for region in regions:
    with open(f'./data/{region}.json', encoding='utf-8') as f:
        price_files[region] = json.load(f)

# Offer names - can be SKU or Managed disk name
offers = jmespath.search("offers | keys(@)", price_files['europe-west'])


offers_formatted = []
for offer in offers:
    offer_formatted = {
        "offer": offer,
        "prices": []
    }        
    for region in regions:
        price_file = price_files[region]    
        query = f"offers.\"{offer}\".prices.perhour.\"{region}\".value"
        sku = jmespath.search(query, price_file)
        offer_formatted["prices"].append({
            "region": region,
            "price": sku
        })

    offers_formatted.append(offer_formatted)
               
with open(output_json, 'w') as f:
    json.dump(offers_formatted, f, indent=4)




# Convert this to a csv file
with open(output_json, 'r') as f:
    data = json.load(f)

    # Write CSV file with the following columns: vm, europe-west, europe-north, germany-west-central, sweden-central
    with open(output_csv, 'w', newline='\n') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerow(['vm', 'sweden-central', 'europe-west', 'europe-north', 'germany-west-central', 'france-central'])
        for offer in data:
            writer.writerow([offer['offer'], offer['prices'][0]['price'], offer['prices'][1]['price'], offer['prices'][2]['price'], offer['prices'][3]['price'], offer['prices'][4]['price']])
