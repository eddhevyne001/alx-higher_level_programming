#!/usr/bin/python3
"""My Int class module"""


class MyInt(int):
    """A My Int class"""
    def __eq__(self, other):
        """Overides and inverts == operator"""
        return int(self) != int(other)

    def __ne__(self, other):
        """Overides and inverts != operator"""
        return int(self) == int(other)
