# Timer

An easy to use python class to handle time measurements in code. 

Instantiate the class and insert one-liners (`take_time`) between your existing code to take timestamps. 
Call the `fancy_print` function to print a nicely formatted overview of how much time has passed overall, how much time has passed between the `take_time` calls, including percentage per step and passed step-descriptions. 


## Logic 

#### Initialization:  `Timer(decimals_time=".4f", decimals_percentage=".2f")`

The optional parameters determine how many decimal values of seconds / of percentage values should be shown. 


#### Function `T.take_time(description="")`:  

The optional parameter `description` is used describe the step and is shown in the `fancy_print` function. 

Use this function with a description of what happened right before it. 

####  Function `T.fancy_print(empty=True)`: 

The optional parameter `empty` is used to empty the existing list of timestamps taken. 
This is useful when implemented in a loop where each iteration needs to be timed independently. 

If the list should not be emptied and you want further timestamps to be appended to the existing ones after printing the overview, set the parameter to `False`.

## Example 

```
import time 

T = Timer()  # Initialization
T.take_time()  # First time is taken 

# some code doing xyz
time.sleep(2)
T.take_time("doing xyz")

# some code doing abc
time.sleep(10)
T.take_time("doing abc")

# some code doing hfg
time.sleep(5)
T.take_time("doing hfg")

T.fancy_print()

```

The printed messages: 
```
------ Time measurements ------
Overall: 17.0243 seconds
Step 0:  2.0136 seconds -  11.83 % - Description: doing xyz
Step 1: 10.0102 seconds -  58.80 % - Description: doing abc
Step 2:  5.0005 seconds -  29.37 % - Description: doing hfg
```
