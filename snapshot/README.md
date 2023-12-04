# Extraction of all osmosis accounts:
With an osmosis node fixed at snapshot block (8269307),
The following was executed (command line):
curl http://0.0.0.0:1317/cosmos/auth/v1beta1/accounts?pagination.limit=9999999999999999 > alltheaccounts.txt


Then the python algorithms selected here with the help of the REST API again, will aid filtering the accounts that had locked osmosis at the time of the snapshot.
