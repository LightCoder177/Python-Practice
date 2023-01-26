# Common functions for my programs.
# or desperate times, desperate measures.

# DateFormat checker.

import re
from datetime import datetime

# Functions


def DateFormat(Date: str) -> bool:
    """Check the date format of the string
     and return either True or False value."""
    r = re.compile(".*/.*/.*")
    m = re.compile(".*-.*-.*")
    if (
        r.match(Date) and
        len(Date) == 10
    ):
        return True

    else:
        return False


def CheckDay(day: int) -> bool:
    """Return a True value if the day <= 31.
    Return a false value if the day > 31."""
    if day <= 31:
        return True
    elif day > 31:
        return False


def CheckMonth(month: int) -> bool:
    """Return a True value if the month <= 12.
    Return a False value if the month >= 12."""
    if month <= 12:
        return True
    elif month >= 12:
        return False


def ValidateDate(date_string: str) -> bool:
    """Check the format of the date."""
    try:
        if date_string != datetime.strptime(
                                            date_string,
                                            "%d/%m/%Y"
        ).strftime("%d/%m/%Y"):
            raise ValueError
        return True
    except ValueError:
        return False
