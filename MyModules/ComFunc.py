# Common functions for my programs.
# or desperate times, desperate measures.

# DateFormat checker.

import re

# Functions


def DateFormat(Date: str) -> bool:
    """Check the date format of the string
     and return either True or False value."""
    r = re.compile(".*/.*/.*")
    m = re.compile(".*-.*-.*")
    if (
        r.match(Date) or m.match(Date) and
        len(Date) == 10
    ):
        return True

    else:
        return False
