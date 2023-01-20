# Creating a program that will check your date
# if it's an even number or odd number.

# importing DateFormat, CheckDay, and CheckMonth
# from ComFunc.

from ComFunc import DateFormat, CheckDay, CheckMonth
import datetime

# Even and odd list.

odd = tuple(range(1, 33, 2))
even = tuple(range(0, 32, 2))

# Conditional loop, conditions, and executions.

while True:
    Date = input("Please type your date here as DD/MM/YYYY: ")

    d = None

    while True:
        if len(Date) == 10:
            Date = Date.split('/')
            Day, Month, Year = [int(item) for item in Date]

            if (
                CheckDay(Day) is True and
                CheckMonth(Month) is True
            ):
                if (
                    Day in odd and
                    Month in odd and
                    (Year-2000) in odd
                ):
                    d = datetime.date(Year, Month, Day)
                    print("Your date is an odd number.")
                    break

                else:
                    print()
                    d = datetime.date(Year, Month, Day)
                    print("Your date is an even number.")
                    break

            else:
                print(
                    "Your day is higher than 31 or "
                    "Your month is higher than 12."
                )
                break

        else:
            print()
            print(
                  "Your date format is incorrect. "
                  "Please enter the correct format."
            )
            break

    if bool(d) is True:
        break
