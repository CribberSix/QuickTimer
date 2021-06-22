import time
from quicktimer import Timer

T = Timer()

# take the starting time, 
T.take_time(description="The description of the first function-call is never displayed!")

time.sleep(5)  # code substitute: parsing the data
T.take_time("Parsed the data", True)

time.sleep(1)  # code substitute: transforming the data
T.take_time("Transformed the data")

time.sleep(2)
T.take_time() 

time.sleep(10)  # code substitute: Storing the data
T.take_time("Stored the data", True)

T.fancy_print()
