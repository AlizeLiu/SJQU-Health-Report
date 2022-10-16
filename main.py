import os
from GenchAPI import GenchAPI
GenchAPI.sign(os.environ.get('username') , os.environ.get('password'))
