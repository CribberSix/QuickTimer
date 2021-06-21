# Timer

An easy to use python class to handle time measurement in code. 

Instantiate the class and insert one-liners (`take_time`) between your existing code to take timestamps. 
Call the `fancy_print` function to print an overview of how much time has passed between which `take_time` calls. 


## Logic 

#### Initialization:  `Timer(decimals=".4f")`

The optional parameter `decimals` determines how many decimal values of seconds should be shown. 


#### Function `T.take_time(description="")`:  

The optional parameter `description` is used describe the step and is shown in the `fancy_print` functions. 

####  Function `T.fancy_print(empty=True)`: 

The optional parameter `empty` is used to empty the existing list of timestamps taken. 
This is useful when implemented in a loop where each iteration needs to be timed independently. 


## Example 

```
import time 

T = Timer()  # Initialization
T.take_time()  # First time is taken 

# some code doing xyz
time.sleep(2)
T.take_time("xyz")

# some code doing abc
time.sleep(10)
T.take_time("abc")

# some code doing hfg
time.sleep(5)
T.take_time("hfg")

T.fancy_print()

```

The printed messages: 
```
------ Time measurements ------
Overall: 17.0243 seconds
Step 0: 2.0136 seconds - 11.83 % - Description: xyz
Step 1: 10.0102 seconds - 58.8 % - Description: abc
Step 2: 5.0005 seconds - 29.37 % - Description: hfg
```
