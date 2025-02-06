def format_date(day,month,year):
    if month in [1, 3, 5, 7, 8, 10, 12] and 1 <= day <= 31:
        return f"The date is {day} of {month} {year}"
    elif month in [4, 6, 9, 11] and 1 <= day <= 30:
        return f"The date is {day} of {month} {year}"
    elif month == 2 and 1 <= day <= 28:
        return f"The date is {day} of {month} {year}"
    else:
        return None

a =  format_date(30,2,2020)
print(a)
