from datetime import datetime, timedelta


class Timer:

    def __init__(self, time_unit='timedelta', decimals_percentage=2, decimals_time=4, output_func=print):
        """Initializes the class. 

        :param time_unit: Unit in which time measurements are displayed. Acceptable values: "timedelta", "milliseconds", "seconds", defaults to "timedelta"
        :type time_unit: str, optional

        :param decimals_time: decimal places to be shown for time_unit "seconds" or "milliseconds", defaults to 4
        :type decimals_time: int, optional

        :param decimals_percentage: decimal places to be shown for percentages, defaults to 2
        :type decimals_percentage: int, optional

        :param output_func: a function to output messages (e.g. to a log), defaults to print
        _type output_func: function, optional
        """
        self.times = []        
        self._acceptable_time_units =  ["timedelta", "milliseconds", "seconds"]

        if time_unit in self._acceptable_time_units:
            self.time_unit = time_unit
        else:
            raise ValueError(f"'{time_unit}' is not an acceptable time unit. Acceptable units are {self._acceptable_time_units}.")
        self.decimals_time_f = f".{decimals_time}f"
        self.decimals_percentage = decimals_percentage
        self.decimals_percentage_f = f".{decimals_percentage}f"
        self.output_func = output_func if output_func != print else print

    def set_time_unit(self, time_unit):
        """Set the unit in which the time is being displayed. 

        Acceptable values: 
            - "timedelta"
            - "seconds"
            - "milliseconds"

        :param time_unit: Unit in which time measurements are displayed
        :type time_unit: str, optional

        :raises ValueError: when an unacceptable time_unit is passed as parameter. 
        """
        if time_unit not in self._acceptable_time_units: 
            raise ValueError(f"'{time_unit}' is not an acceptable time unit. Acceptable units are {self._acceptable_time_units}.")
        self.time_unit = time_unit

    def set_output_func(self, output_func):
        """Sets the output function of the module.

        :param output_func: a function to output messages (e.g. `logger.info` or `print`)
        :type output_func: function, optional
        """
        self.output_func = output_func

    def take_time(self, description="", printme=False):
        """Snapshots the current time and inserts it into the List as a Tuple with the passed description.

        :param description: Gets saved alongside the timestamp. Use it as a descriptor of what happened before the function was called, defaults to empty String
        :type description: str

        :param printme: Enable printing the description after taking a snapshot of the time. Use this parameter to keep track of the code progress during runtime, defaults to False
        :type printme: bool
        """
        self.times.append((datetime.now(), description))
        if printme:
            self.output_func(description)

    def fancy_print(self, delete=True):
        """Fancy prints the entire time taken, the differences between the individual timestamps in absolute seconds & in percentages as well as the descriptions.

        :param delete: deletes the currently stored list of timestamps after ouput, defaults to True
        :type delete: bool, optional
        """
        r = self._get_individual_differences()
        entire_time = self._get_entire_difference()
        
        self.output_func("------ Time measurements ------")
        if self.time_unit == "seconds": 
            self.output_func(f"Overall: {format(entire_time.total_seconds(), self.decimals_time_f)} seconds")
        elif self.time_unit == "milliseconds": 
            self.output_func(f"Overall: {format(entire_time.total_seconds() * 1000, self.decimals_time_f)} milliseconds")
        else:
            self.output_func(f"Overall: {entire_time}")

        # return early if no steps were recorded
        if len(r) == 0:  
            return  

        # get length of maximum step-string
        step_max_length = len(str(len(r)))  

        # get length of maximum seconds & millisecond-string 
        if self.time_unit == "seconds":   
            time_sec_max_length = max([len(format(x[0].total_seconds(), self.decimals_time_f)) for x in r])  
        elif self.time_unit == "milliseconds": 
            time_ms_max_length = max([len(format(x[0].total_seconds() * 1000, self.decimals_time_f)) for x in r]) 

        # output step: step number, time taken and percentage of time taken by step compared to overall time taken
        for i, e in enumerate(r):
            step = f"{i}".rjust(step_max_length)
            perc = f"{e[1]}".format(1.2).rjust(self.decimals_percentage + 4)

            # format time values and rjust them in case they have differing lengths
            if self.time_unit == "seconds": 
                time = f"{format(e[0].total_seconds(), self.decimals_time_f)}".rjust(time_sec_max_length) + " seconds"
            elif self.time_unit == "milliseconds":
                time = f"{format(e[0].total_seconds() * 1000, self.decimals_time_f)}".rjust(time_ms_max_length) + " milliseconds"
            else: 
                time = f"{e[0]}"

            self.output_func(f"Step {step}: {time} - {perc} % - Description: {e[2]}")
        
        # delete all stored timestamps if set
        if delete:
            self.delete_timestamps()

    def delete_timestamps(self):
        """Deletes any stored timestamps including descriptions."""
        self.times = []

    def _get_individual_differences(self):
        """Calculates individual differences and the percentage for each difference based on the time between the first and last call.

        :return: List of Tuples consisting of timedeltas between steps and description of the step.
        :rtype: List<(datetime.timedelta, str)>
        """

        diffs = []
        for i, _ in enumerate(self.times):
            if i == 0:
                continue
            d = self.times[i][0] - self.times[i-1][0]
            diffs.append((d, self.times[i][1]))


        total = sum([x[0] for x in diffs], timedelta())
        if total > timedelta(seconds=0):
            return [(x[0], format(round((x[0] / total * 100), 2), self.decimals_percentage_f), x[1]) for x in diffs]
        else:
            return [(x[0], format(0, self.decimals_percentage_f), x[1]) for x in diffs]
        
        # [(format(x[0], self.decimals_time_f), format(round((x[0] / total * 100), 2), self.decimals_percentage_f), x[1]) for x in diffs]
        # [(format(x[0], self.decimals_time_f), format(0, self.decimals_percentage_f), x[1]) for x in diffs]


    def _get_entire_difference(self):
        """Returns the difference between the first and the last timestamp."""
        if len(self.times) > 0:
            diff = self.times[-1][0] - self.times[0][0]
            return diff
        else:
            return timedelta(seconds=0)

    def get_timestamps(self):
        """Returns the stored timestamps.

        :return: A list of stored timestamps
        :rtype: List<datetime>
        """
        return [c[0] for c in self.times]

    def get_descriptions(self):
        """Returns the stored descriptions. 
        
        If no description was supplied when `take_time` was called, the value is an empty String. 

        :return: List of stored descriptions.
        :rtype: List<str>
        """
        return [c[1] for c in self.times]

    def get_timestamps(self):
        """Returns the timestamps including the descriptions as a List of Tuples. 

        :return: A list of timestamps and discriptions.
        :rtype: List<(datetime, str)>
        """
        return self.times
