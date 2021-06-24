Example
=============

Installation
*******************

The package is available on `PyPi <https://pypi.org/project/quicktimer/>`_ :

.. code-block:: 

    pip install quicktimer


Usage
**************************************************

Instantiate the :code:`Timer` class and insert one-liners with :code:`take_time()` between your existing code to take timestamps. 

Call the :code:`fancy_print()` function to print a nicely formatted overview of how much time has passed overall, 
how much time has passed between the :code:`take_time` calls, including percentage per step and passed step-descriptions. 

Although both functions (:code:`take_time()` & :code:`fancy_print()`) can be used 
without any parameters, you should pass at least a description to :code:`take_time("Finished x!")` to add some context to your measurements. 

You can either make use of the default output method (:code:`print` to the console) or you can pass a custom function: for instance to pass the messages to a logger. 


Using the default output method
##################################

When no :code:`output_func` parameter is passed during instantiation, it defaults to :code:`print` the messages to the console as follows: 


.. code-block:: python

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



Output of the code in the console: 

.. code-block:: 

    > Stored the data
    > ------ Time measurements ------
    > Overall: 0:00:01.254049
    > Step 0: 0:00:01.113962 -  88.83 % - Description: Parsed the data
    > Step 1: 0:00:00.030001 -   2.39 % - Description: 
    > Step 2: 0:00:00.110086 -   8.78 % - Description: Stored the data


The time can be displayed as :code:`timedelta` (default), :code:`seconds` or :code:`milliseconds`. 
The number of decimal places for :code:`seconds` or :code:`milliseconds` can be set with the parameter :code:`decimals_time` which defaults to :code:`4`. 
The number of decimal places for the :code:`percentages` can be set with the parameter :code:`decimals_percentage` which defaults to :code:`2`. 

When initialized with :code:`T = Timer(time_unit="seconds", decimals_time=2, decimals_percentage=1)` the output would be the following. 

.. code-block:: 

    > Stored the data
    > ------ Time measurements ------
    > Overall: 1.24 seconds
    > Step 0: 1.10 seconds -  88.8 % - Description: Parsed the data
    > Step 1: 0.03 seconds -   2.5 % - Description: 
    > Step 2: 0.11 seconds -   8.8 % - Description: Stored the data


Using a logger as output method 
#################################

Instead of :code:`printing` to the console, you can also pass your own function to the module. 
This can be used with an easily configured :code:`logger` to write the messages to your log.     

.. code-block:: python 

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


The contents of your log-file would look like this: 

.. code-block::  

    2021-06-24 13:35:43,275 [INFO ]  Stored the data
    2021-06-24 13:35:43,275 [INFO ]  ------ Time measurements ------
    2021-06-24 13:35:43,275 [INFO ]  Overall: 0:00:00.624691
    2021-06-24 13:35:43,275 [INFO ]  Step 0: 0:00:00.512639 -  82.06 % - Description: Parsed the data
    2021-06-24 13:35:43,275 [INFO ]  Step 1: 0:00:00.112052 -  17.94 % - Description: Stored the data
