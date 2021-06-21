from datetime import datetime


class Timer:

    def __init__(self, decimals=".4f"):
        self.times = []
        self.decimals = decimals

    def take_time(self, description=""):
        """Snapshots the current time and inserts it into the List as a Tuple with the passed description."""
        self.times.append((datetime.now(), description))

    def fancy_print(self, empty=True):
        """Fancy prints the differences between the individuals and the entire time taken."""
        r = self._get_individual_differences()
        entire_time = self._get_entire_difference()
        print("------ Time measurements ------")
        print(f"Overall: {entire_time} seconds")
        for i, e in enumerate(r):
            print(f"Step {i}: {e[0]} seconds - {e[1]} % - Description: {e[2]}")
        if empty:
            self._empty_time()

    def _empty_time(self):
        """Resets the list."""
        self.times = []

    def _get_individual_differences(self):
        """Calculates individual differences and percentage for each difference of the whole."""
        diffs = []
        for i, _ in enumerate(self.times):
            if i == 0:
                continue
            d = self.times[i][0] - self.times[i-1][0]
            diffs.append((d.total_seconds(), self.times[i][1]))
        total = sum([x[0] for x in diffs])
        if total > 0:
            return [(format(x[0], self.decimals), round((x[0] / total * 100), 2), x[1]) for x in diffs]
        else:
            return [(format(x[0], self.decimals), 0, x[1]) for x in diffs]

    def _get_entire_difference(self):
        """Returns the difference between the first and the last timestamp."""
        if len(self.times) > 0:
            diff = self.times[-1][0] - self.times[0][0]
            return format(diff.total_seconds(), self.decimals)
        else:
            return None
