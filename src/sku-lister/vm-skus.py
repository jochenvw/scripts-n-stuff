import json
import jmespath

# Regions to find SKU numbers for
regions = ['global','sweden-central', 'europe-west', 'europe-north', 'germany-west-central']

# Get input.json as follows
# - https://azure.microsoft.com/en-us/pricing/calculator/ - start fresh
# - Add Virtual Machines to cost
# - Log in (bottom of the page)
# - F12 dev tools - Network tab - clean it up
# - Hit 'Display Part Numbers' button at bottom of the page
# - Find the 5-6 meg download - save as input.json

input = './data/vms_in.json'
output = './data/vms_out.json'

with open(input) as f:
    data = json.load(f)

# Offer names - can be SKU or Managed disk name
offers = jmespath.search("offers | keys(@)", data)

offers_formatted = []
for offer in offers:
    offer_formatted = {
        "offer": offer,
        "regionalSKUs": []
    }        
    for region in regions:
        query = f"offers.\"{offer}\".partNumbers.\"{region}\".sku"
        sku = jmespath.search(query, data)
        offer_formatted["regionalSKUs"].append({
            "region": region,
            "SKU": sku
        })

    offers_formatted.append(offer_formatted)
               
with open(output, 'w') as f:
    json.dump(offers_formatted, f, indent=4)