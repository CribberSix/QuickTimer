from datetime import datetime


class Timer:

    def __init__(self, decimals_time=4, decimals_percentage=2, output_func=print):
        """Initializes the class. 

        :param decimals_time: decimal places to be shown for seconds, defaults to 4
        :type decimals_time: int, optional
        :param decimals_percentage: decimal places to be shown for percentages, defaults to 2
        :type decimals_percentage: int, optional
        :param output_func: a function to output messages (e.g. to a log), defaults to print
        _type output_func: function, optional
        """
        self.times = []
        self.decimals_time = f".{decimals_time}f"
        self.decimals_percentage = f".{decimals_percentage}f"
        self.output_func = output_func if output_func != print else print
    

    def set_output_func(self, output_func=print):
        """Sets the output function of the module.

        :param output_func: a function to output messages (e.g. to a log), defaults to print
        :type output_func: function, optional
        """
        self.output_func = output_func if output_func != print else print

    def take_time(self, description="", printme=False):
        """Snapshots the current time and inserts it into the List as a Tuple with the passed description.

        :param description: Gets saved alongside the timestamp. Use it as a descriptor of what happened before the function was called.
        :type description: str

        :param printme: Enable printing the description after taking a snapshot of the time. Use this parameter to keep track of the code progress during runtime.
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
        self.output_func(f"Overall: {entire_time} seconds")
        if len(r) == 0: 
            return 

        step_max_length = len(str(len(r)))  # get length of maximum step-string
        second_max_length = max([len(x[0]) for x in r])  # get length of maximum seconds-string      
        for i, e in enumerate(r):
            step = f"{i}".rjust(step_max_length)
            secs = f"{e[0]}".rjust(second_max_length)
            perc = f"{e[1]}".format(1.2).rjust(6)
            self.output_func(f"Step {step}: {secs} seconds - {perc} % - Description: {e[2]}")
        if delete:
            self.delete_timestamps()

    def delete_timestamps(self):
        """Deletes any stored timestamps including descriptions."""
        self.times = []

    def _get_individual_differences(self):
        """Calculates individual differences and the percentage for each difference based on the time between the first and last call."""
        diffs = []
        for i, _ in enumerate(self.times):
            if i == 0:
                continue
            d = self.times[i][0] - self.times[i-1][0]
            diffs.append((d.total_seconds(), self.times[i][1]))
        total = sum([x[0] for x in diffs])
        if total > 0:
            return [(format(x[0], self.decimals_time), format(round((x[0] / total * 100), 2), self.decimals_percentage), x[1]) for x in diffs]
        else:
            return [(format(x[0], self.decimals_time), format(0, self.decimals_percentage), x[1]) for x in diffs]

    def _get_entire_difference(self):
        """Returns the difference between the first and the last timestamp."""
        if len(self.times) > 0:
            diff = self.times[-1][0] - self.times[0][0]
            return format(diff.total_seconds(), self.decimals_time)
        else:
            return None

    def get_timestamps(self):
        """Returns the stored timestamps.

        :return: A list of stored timestamps
        :rtype: List<datetime>
        """
        return [c[0] for c in self.times]

    def get_descriptions(self):
        """Returns the stored descriptions. 
        
        If no description was supplied when `take_time` was called, the value is an empty string. 

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
