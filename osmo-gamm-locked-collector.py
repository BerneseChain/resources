import json
import os

# Open the .txt file and load JSON content
with open('alltheaccounts.txt', 'r') as file:
    data = json.load(file)

# Print header
print("Address,Amount")

# Extract addresses and print them
for account in data.get('accounts', []):
    address = account.get('address')

    # Make the curl request
    response = os.popen(f'curl -s localhost:1317/osmosis/lockup/v1beta1/account_locked_coins/{address}').read()

    # Parse the response as JSON
    response_data = json.loads(response)

    # Check if the desired denomination is present in the coins list
    desired_denom = "gamm/pool/662"
    coins = response_data.get('coins', [])
    amount = next((coin.get('amount') for coin in coins if coin.get('denom') == desired_denom), None)

    if amount is not None:
        print(f'{address},{amount}')

