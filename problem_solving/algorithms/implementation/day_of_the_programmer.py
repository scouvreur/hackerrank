
def is_leap_year(calendar: str, year: int) -> bool:
    if calendar == "julian":
        return year%4 == 0
    elif calendar == "gregorian":
        return (year%400 == 0) or ((year%4 == 0) and (year%100 != 0))


def day_of_programmer(year: str) -> str:
    year = int(year)

    if (year >= 1700) and (year < 1918):
        calendar = "julian"
    else:
        calendar = "gregorian"

    if is_leap_year(calendar, year):
        return "12.09.{}".format(year)
    elif year == 1918:
        # in 1918 Russia switched from the
        # Julian to the Gregorian calendar
        return "26.09.1918"
    else:
        return "13.09.{}".format(year)

def test_is_leap_year():
    """Test for the is_leap_year function."""
    assert is_leap_year("julian", 1800) is True
    assert is_leap_year("gregorian", 1984) is True


def test_day_of_programmer():
    """Test for the day_of_programmer function."""
    assert day_of_programmer("2016") == "12.09.2016"
    assert day_of_programmer("1800") == "12.09.1800"
    assert day_of_programmer("2015") == "13.09.2015"
    assert day_of_programmer("1918") == "26.09.1918"

test_is_leap_year()
# test_day_of_programmer()
