import time
from quicktimer import Timer

T = Timer()

# take the starting time
T.take_time(description="The description of the first function-call is not displayed!")

time.sleep(1.1)  # code substitute: parsing the data
T.take_time("Parsed the data")

time.sleep(0.02)  # code substitute
T.take_time() 

time.sleep(0.1) # code substitute: Storing the data
T.take_time("Stored the data", True)

T.fancy_print()
