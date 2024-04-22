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
with open('./input.json') as f:
    data = json.load(f)

vms = jmespath.search("offers | keys(@)", data)

vm_skus = []
for vm in vms:
    vm_sku = {
        "vm": vm,
        "skus": []
    }        
    for region in regions:
        query = f"offers.\"{vm}\".partNumbers.\"{region}\".sku"
        sku = jmespath.search(query, data)
        vm_sku["skus"].append({
            "region": region,
            "sku": sku
        })

    vm_skus.append(vm_sku)
               
with open('./output.json', 'w') as f:
    json.dump(vm_skus, f, indent=4)
