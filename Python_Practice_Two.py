# A program that will ask the date
# from the user and will tell if the
# year, month, day in the date are even
# or odd numbers.

# importing DateFormat from ComFunc.
# importing datetime module.

from ComFunc import DateFormat
import datetime

# Odd and Even list.

odds = list(range(1, 33, 2))
even = list(range(0, 32, 2))

# conditional loop, input variable, conditions,
# and execution.

while True:
    Date = input("Please enter the date as DD/MM/YYYY: ")

    if DateFormat(Date) is True:
        Day, Month, Year = map(int, Date.split('/'))
        UserDate = datetime.date(Year, Month, Day)

        if (
            Day in odds and
            Month in odds and
            (Year-2000) in odds
        ):
            print("Your date is an odd number.")
            break

        elif (
              Day in even or
              Month in even or
              (Year-2000) in odds
        ):
            print("Your day, month, or year is an even number.")
            break

    elif DateFormat(Date) is False:
        print()
        print("That's not the correct format.")
