import os
from GenchAPI import GenchAPI
GenchAPI.sign(os.environ.get('USERNAME') , os.environ.get('PASSWORD'))
