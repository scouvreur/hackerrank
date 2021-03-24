def count_substring(string, sub_string):
    """
    asdalskdm
    """
    if sub_string not in string:
        return 0
    else:
        return string.find(sub_string)


def test_count_substring():
    """Test for count_substring function."""
    assert count_substring(string="ABCDCDC", sub_string="CDC") == 2


test_count_substring()
string = input().strip()
sub_string = input().strip()
count = count_substring(string, sub_string)
print(count)
