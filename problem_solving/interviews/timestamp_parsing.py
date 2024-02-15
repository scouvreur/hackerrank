"""
Write a function that parses a string timestamp, similar to what is provided
by Kubernetes using `kubectl get pods` in the `AGE` column, and returns the
number of seconds as a integer.

```bash
>>> kubectl -n <NAMESPACE> get pods
NAME                      READY   STATUS             RESTARTS        AGE
pod-1-5mbz6               1/1     Running            0               7d2h
pod-1-9w9n6               1/1     Running            0               4d1h
```

Example:
"1h23m45s" should return 5025 seconds

It should handle inputs like:
"1h23m45s" -> 1h, 23m
"23m45s"
"23m"
"1d1h"
"""

def parse_timestamp(s: str) -> int:
    # initialize values
    days = 0
    hours = 0
    minutes = 0
    seconds = 0

    # check for day component
    if "d" in s:
        days_str = s.split("d")[0]
        days = int(days_str)
        s = s[len(days_str)+1:]

    # check for hour component
    if "h" in s:
        hours_str = s.split("h")[0]
        hours = int(hours_str)
        s = s[len(hours_str)+1:]

    # check for minute component
    if "m" in s:
        minutes_str = s.split("m")[0]
        minutes = int(minutes_str)
        s = s[len(minutes_str)+1:]

    # check for second component
    if "s" in s:
        seconds_str = s.split("s")[0]
        seconds = int(seconds_str)
        s = s[len(seconds_str)+1:]

    total_seconds = 24*60*60*days + 60*60*hours + 60*minutes + seconds

    return total_seconds

def test_parse_timestamp():
    """Test for parse_timestamp function."""
    assert parse_timestamp("1h23m45s") == 5025
    assert parse_timestamp("23m") == 1380
    assert parse_timestamp("1d1h") == 86400 + 3600
    # What inputs might break your function ?
    # "0d0h0mXs"
    # "1d1w23s30m"
    # "word"
    # "0d Od"
    # "-1d"
    # ""


test_parse_timestamp()
