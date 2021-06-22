Examples
=============

Installation
*******************
As the package has not been published on PyPi yet, it CANNOT be install using pip.


Usage
**************************************************

The two main commands are :code:`take_time()` and :code:`fancy_print()`.

Both can be used without any parameters, although you should pass at least a description to :code:`take_time("Finished x!")` to make full use of this module. 

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

.. code-block:: python

    > Parsed the data
    > Stored the data
    > ------ Time measurements ------
    > Overall: 18.0395 seconds
    > Step 0:  5.0140 seconds -  27.79 % - Description: Parsed the data
    > Step 1:  1.0059 seconds -   5.58 % - Description: Transformed the data
    > Step 2:  2.0148 seconds -  11.17 % - Description: 
    > Step 3: 10.0048 seconds -  55.46 % - Description: Stored the data

That's it!
