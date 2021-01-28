import logging
import os
from os import environ


# Set environment variables
os.environ['API_USER'] = 'rimma'

# Get environment variables
USER = os.getenv('API_USER')

# setting up logging
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger()
logger.addHandler(logging.FileHandler('test.log', 'a'))
print = logger.info

# cheking if env var is visable, if yes writtin to log
if environ.get('USER') is not None:
    print('env var is visable USER: ' + USER) 

