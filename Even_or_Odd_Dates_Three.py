# Creating a program that will check your date
# if it's an even or odd number.

# importing CheckDay and CheckMonth
# from ComFunc module.
# importing datetime module.

from ComFunc import CheckDay, CheckMonth, ValidateDate, OverlapDates
import datetime


# Even and odd tuples.

odd = tuple(range(1, 10000, 2))
even = tuple(range(0, 10000, 2))


# Conditional loops, conditions, and executions

while True:
    Date = input("Please type your date here as DD/MM/YYYY: ")

    d = None

    if ValidateDate(Date) is True:
        Date = Date.split('/')
        Day, Month, Year = [int(item) for item in Date]

        if (
            CheckDay(Day) is True and
            CheckMonth(Month) is True
        ):
            if (
                Day in odd and
                Month in odd and
                Year in odd
            ):
                d = datetime.date(Year, Month, Day)
                print("Your date is an odd number.")
                break

            elif (
                   Day in even and
                   Month in even and
                   Year in even
            ):
                d = datetime.date(Year, Month, Day)
                print("Your date is an even number.")
                break

            elif OverlapDates(
                              Day=Day,
                              Month=Month,
                              Year=Year
            ) is True:
                print()
                d = datetime.date(Year, Month, Day)
                print("{0:d}/{1:d}/{2:d}".format(Day, Month, Year))
                print("Your date is overlapping in the even and odd list.")
                break

            else:
                d = datetime.date(Year, Month, Day)
                print("Your date are nor even or odd numbers.")

        else:
            print()
            print("Your day or month is higher than 31 days or 12 month.")
            break
    elif ValidateDate(Date) is False:
        print()
        print("Your format is incorrect.")
        print("Please type the correct format.")

    if bool(d) is True:
        break
