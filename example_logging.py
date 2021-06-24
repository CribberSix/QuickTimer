import time
import logging
from quicktimer import Timer

# setting up a logger
my_format = "%(asctime)s [%(levelname)-5.5s]  %(message)s"
logging.basicConfig(filename='test.log', level=logging.INFO, format=my_format)
logger = logging.getLogger()

# Using the package
T = Timer(output_func=logger.info)
T.take_time()  # take the starting time

time.sleep(0.5)  # code substitute: parsing the data
T.take_time("Parsed the data", True)

time.sleep(0.1)  # code substitute: Storing the data
T.take_time("Stored the data", True)

T.fancy_print()

