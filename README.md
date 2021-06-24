[![PyPi](https://img.shields.io/pypi/v/quicktimer?color=blue&style=plastic)](https://pypi.org/project/quicktimer/)
![License](https://img.shields.io/pypi/l/quicktimer?style=plastic)
[![CodeFactor](https://www.codefactor.io/repository/github/cribbersix/quicktimer/badge?style=plastic)](https://www.codefactor.io/repository/github/cribbersix/quicktimer)
![Repository size](https://img.shields.io/github/repo-size/Cribbersix/QuickTimer?style=plastic)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg?style=plastic)](https://www.python.org/)


# Timer

An easy to use python package to handle time measurements in code. 

Instantiate the `Timer` class and insert one-liners with `take_time()` between your existing code to take timestamps. 

Call the `fancy_print()` function to print a nicely formatted overview of how much time has passed overall, how much time has passed between the `take_time()` calls, including percentage per step and passed step-descriptions. 


# Installation

The package is available on [PyPi](https://pypi.org/project/quicktimer/) :

```
pip install quicktimer 
```

# Usage

The entire functionality is documented in-depth on [readthedocs](https://quicktimer.readthedocs.io/en/latest/quicktimer.html#module-quicktimer).
In the following a quick overview of the basic functionality is shown. 

The two main commands are `take_time()` and `fancy_print()`.

Both can be used without any parameters, although you should pass at least a description to `take_time("Finished x!")` to add some context to your measurements. 

You can either make use of the default output method (`print` to the console) or you can pass a custom function: for instance to pass the messages to a logger. 

### Using the default output method (print)

When no `output_func` parameter is passed during instantiation, it defaults to `print` the messages to the console as follows: 


```python
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
```

Output of the code in the console: 

```
> Stored the data
> ------ Time measurements ------
> Overall: 0:00:01.254049
> Step 0: 0:00:01.113962 -  88.83 % - Description: Parsed the data
> Step 1: 0:00:00.030001 -   2.39 % - Description: 
> Step 2: 0:00:00.110086 -   8.78 % - Description: Stored the data
```


### Using a logger as output method 

Instead of `printing` to the console, you can also pass your own function to the module. 
This can be used with an easily configured `logger` to write the messages to your log.   

```python 
import time
import logging
from quicktimer import Timer

# setting up a logger
my_format = "%(asctime)s [%(levelname)-5.5s]  %(message)s"
logging.basicConfig(filename='test.log', level=logging.INFO, format=my_format)
logger = logging.getLogger()

# logger.info will be used as the output function instead of print
T = Timer(output_func=logger.info)  

T.take_time()  # take the starting time
time.sleep(0.5)  # code substitute: parsing the data
T.take_time("Parsed the data")
time.sleep(0.1)  # code substitute: Storing the data
T.take_time("Stored the data", True)

T.fancy_print()
```
