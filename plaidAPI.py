import json
from plaid.api import Client
from plaid.errors import PlaidError

client = Client(client_id='id', secret='secret', environment='sandbox')

# Create a link token
try:
    response = client.LinkToken.create(
        {
            'user': {
                'client_user_id': 'user-id',
            },
            'client_name': "Your App Name",
            'products': ['transactions','income','assets'],
            'country_codes': ['US'],
            'language': 'en',
        }
    )
    link_token = response['link_token']
except PlaidError as e:
    print(e.code, e.message)
    exit()

# Use the link token where you need it

# Request transactions
try:
    response = client.Transactions.get(link_token, start_date='2022-01-01', end_date='2022-01-31')
    transactions = response['transactions']
    
    # Store transactions as JSON file
    with open('transactions.json', 'w') as file:
        json.dump(transactions, file)
    print("Transactions stored in transactions.json")
        
except PlaidError as e:
    print("Error:", e)
