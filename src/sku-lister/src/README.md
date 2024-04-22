# SKU Lister

## Pre-req: download SKU info

Get the SKU info from the Azure Pricing Calculator.  This is a 5-6 meg JSON file that contains all the SKU info for Azure services.  It is used to map the SKU to the service name.

Get input.json as follows:

- [https://azure.microsoft.com/en-us/pricing/calculator/](https://azure.microsoft.com/en-us/pricing/calculator/) - start fresh (delete all items)
- Add Virtual Machines to cost
- Log in (bottom of the page):
- F12 dev tools - Network tab - clean it up:
- Hit 'Display Part Numbers' button at bottom of the page:
- Find the 5-6 meg download - save as input.json`:
