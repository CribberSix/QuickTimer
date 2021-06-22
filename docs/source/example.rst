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

Call the :code:`fancy_print()` function to print a nicely formatted overview of how many seconds have passed overall, how many seconds have passed between the `take_time` calls, including percentage per step and passed step-descriptions. 

Although both functions (:code:`take_time()` & :code:`fancy_print()`) can be used 
without any parameters, you should pass at least a description to :code:`take_time("Finished x!")` to make full use of this module. 

.. code-block:: python

    import time
    from quicktimer import Timer

    T = Timer()

    # take the starting time
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



Output of the code: 

.. code-block:: 

    > Parsed the data
    > Stored the data
    > ------ Time measurements ------
    > Overall: 18.0395 seconds
    > Step 0:  5.0140 seconds -  27.79 % - Description: Parsed the data
    > Step 1:  1.0059 seconds -   5.58 % - Description: Transformed the data
    > Step 2:  2.0148 seconds -  11.17 % - Description: 
    > Step 3: 10.0048 seconds -  55.46 % - Description: Stored the data

That's it!
