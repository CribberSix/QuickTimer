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

Call the :code:`fancy_print()` function to print a nicely formatted overview of how many seconds have passed overall, how many seconds have passed between the :code:`take_time` calls, including percentage per step and passed step-descriptions. 

Although both functions (:code:`take_time()` & :code:`fancy_print()`) can be used 
without any parameters, you should pass at least a description to :code:`take_time("Finished x!")` to add some context to your measurements. 

You can either make use of the default output method (:code:`print` to the console) or you can pass a custom function: for instance to pass the messages to a logger. 


Using the default output method :code:`print`
****************************************************************************************************

When no :code:`output_func` parameter is passed during instantiation, it defaults to :code:`print` the messages to the console as follows: 


.. code-block:: python

    import time
    from quicktimer import Timer

    T = Timer()

    # take the starting time
    T.take_time(description="The description of the first function-call is never displayed!")

    time.sleep(5)  # code substitute: parsing the data
    T.take_time("Parsed the data")

    time.sleep(2)  # code substitute
    T.take_time() 

    time.sleep(10) # code substitute: Storing the data
    T.take_time("Stored the data", True)

    T.fancy_print()



Output of the code in the console: 

.. code-block:: 

    > Stored the data
    > ------ Time measurements ------
    > Overall: 17.0340 seconds
    > Step 0:  5.0119 seconds -  29.42 % - Description: Parsed the data
    > Step 1:  2.0085 seconds -  11.79 % - Description: 
    > Step 2: 10.0136 seconds -  58.79 % - Description: Stored the data




Using a logger as output method 
****************************************************************************************************

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
