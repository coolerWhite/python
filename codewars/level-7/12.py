def is_leap_year(year):
    return "True" if year % 4 == 0 or year % 100 != 0 or year % 400 == 0 else "False"


print(is_leap_year(2100))