#!/bin/python3


def time_conversion(s):
    if "AM" in s:
        hour = str(int(s[:2])%12).zfill(2)
        return (hour + s[2:]).replace("AM", "")
    elif "PM" in s:
        hour = str(int(s[:2])+12).zfill(2)
        if hour == "24":
            hour = "12"
        return (hour + s[2:]).replace("PM", "")


def test_time_conversion():
    """Test the time conversion function."""
    assert time_conversion(s="07:05:45PM") == "19:05:45"
    assert time_conversion(s="07:05:45AM") == "07:05:45"
    assert time_conversion(s="11:05:45PM") == "23:05:45"
    assert time_conversion(s="12:00:00AM") == "00:00:00"
    assert time_conversion(s="12:45:54PM") == "12:45:54"
    assert time_conversion(s="12:05:39AM") == "00:05:39"
    assert time_conversion(s="12:40:22AM") == "00:40:22"


test_time_conversion()
s = input()
result = time_conversion(s)
print(result)
