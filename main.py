import sys
from GenchAPI import GenchAPI
username = sys.argv[1]
password = sys.argv[2]
print(username, password)
GenchAPI.sign(username, password)
