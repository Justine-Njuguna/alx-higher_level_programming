#!/usr/bin/python3


class MyList(list):
    """Custom list class inheritance from the built-in list class"""

    def print_sorted(self):
        """print the list in ascending sorted order"""

        sorted_list = sorted(self)
        print(sorted_list)
