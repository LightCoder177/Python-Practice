# Checking your date if it is
# even or odd number

# importing ValidateDate and Overlapping functions
# from Comfunc.

from ComFunc import ValidateDate, OverlapDates

# list and variable.

odd = list(range(1, 10000, 2))
even = list(range(0, 10000, 2))

Date = None
Repeat_or_not = None

# Welcome message.

print("Welcome to my humble program.")

# conditional loop, conditions, and executions.

while True:
    Date = input("Please enter your date as dd/mm/yyyy: ")

    if ValidateDate(Date) is True:
        date = Date.split('/')
        Day, Month, Year = [int(item) for item in date]

        if (
            Day in odd and
            Month in odd and
            Year in odd
        ):
            print()
            print("Your date is an odd number.")

        elif (
              Day in even and
              Month in even and
              Year in even
        ):
            print()
            print("Your date is an even number.")

        elif OverlapDates(
                          Day=Day,
                          Month=Month,
                          Year=Year
        ):
            print()
            print("Your date is overlapping in both even and odd list.")

    else:
        print("That's not the correct format.")
        print()

    while True:
        Repeat_or_not = input(
            "Would you like to try again? Type 'Yes' or 'No': ").lower()

        if Repeat_or_not == "yes":
            print()
            print("Please re-enter the date.")
            break

        elif Repeat_or_not == "no":
            print()
            print("Thanks for trying my program. Allah bless you.")
            break

        else:
            print("That's not the correct answer.")
    if Repeat_or_not == "no":
        break
