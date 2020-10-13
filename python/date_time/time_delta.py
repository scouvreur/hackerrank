from datetime import datetime


def time_delta(t1, t2):
    """
    Takes two datetime strings in the
    following format :
        Sun 10 May 2015 13:54:36 -0700
    and returns the time difference in
    seconds between them.

    Parameters
    ----------
    t1, t2 : string
        Input two timestamps to compute
        difference on.

    Returns
    -------
    delta_t : int
        Time difference in seconds between t1 and t2.
    """
    time_format = "%a %d %b %Y %H:%M:%S %z"
    t1 = datetime.strptime(t1, time_format)
    t2 = datetime.strptime(t2, time_format)
    delta_t = int(abs((t1 - t2).total_seconds()))
    print(delta_t)
    return delta_t


def test_time_delta():
    # Tests function with two sample cases
    assert (
        time_delta(
            "Sun 10 May 2015 13:54:36 -0700", "Sun 10 May 2015 13:54:36 -0000"
        )
        == 25200
    )
    assert (
        time_delta(
            "Sat 02 May 2015 19:54:36 +0530", "Fri 01 May 2015 13:54:36 -0000"
        )
        == 88200
    )


test_time_delta()
