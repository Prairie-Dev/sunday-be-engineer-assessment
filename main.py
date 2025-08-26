import datetime
import json
from dateutil.parser import parse

'''
## Scenario:
# We have the following list of products for a customer.  Each product has a date on which it should be applied to the customer's lawn. Each product also has a quantity that indicates how many physical bags of product are being sent (and should be applied).

## Task:
# Write a function that takes the following list of products and returns an array of shipments each with their own shipment_date with included products
#    - You must use more than 1 shipment, but no more than 4
#    - Each shipment must have a shipment_date so that the customer receives the product before their application_date
'''

products = [
    {
      "name": "Lawn Strong",
      "quantity": 2,
      "application_date": "2024-05-29",
    },
    {
      "name": "Lawn Aid",
      "quantity": 2,
      "application_date": "2024-06-25",
    },
    {
      "name": "Green Out",
      "quantity": 4,
      "application_date": "2024-07-30",
    },
    {
      "name": "Drought Defense",
      "quantity": 1,
      "application_date": "2024-07-27",
    },
    {
      "name": "Iron Boost",
      "quantity": 2,
      "application_date": "2024-08-15",
    },
    {
      "name": "Fall Fortify",
      "quantity": 1,
      "application_date": "2024-09-22",
    }
  ]

def group_shipments(products):
    pass

shipments = group_shipments(products)
