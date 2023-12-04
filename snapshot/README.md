# Extraction of all osmosis accounts:
With an osmosis node fixed at snapshot block (8269307),
The following was executed (command line):


curl http://0.0.0.0:1317/cosmos/auth/v1beta1/accounts?pagination.limit=9999999999999999 > alltheaccounts.txt

# Filter algo: osmo-gamm-locked-collector.py

Then the python algorithm contained in this repository (osmo-gamm-locked-collector.py) selected here with the help of the REST API again, will aid filtering the accounts that had locked osmosis at the time of the snapshot.

# Query for locked gamm tokens
The type of the query done is as follows:

for example
curl localhost:1317/osmosis/lockup/v1beta1/account_locked_coins/osmo1lllpx9z628vxf8aav728ngze0l0alq3ge3rvdz
