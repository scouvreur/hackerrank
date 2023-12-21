def encrypt(input: str) -> str:
    output = ""
    i = 0
    while i < len(input) - 1:
        if input[i].islower() and input[i + 1].isupper():
            output += input[i + 1] + input[i] + "*"
            i += 2
        elif input[i].isdigit():
            output = input[i] + output + "0"
            i += 1
        else:
            output += input[i]
            i += 1

    output += input[i]
    return output


def test_encrypt():
    """
    Test for the encrypt function.
    """
    assert encrypt("hAck3rr4nk") == "43Ah*ck0rr0nk"
    assert encrypt("aP1pL5e") == "51Pa*0Lp*0e"
    assert encrypt("poTaTO") == "pTo*Ta*O"


def decrypt(input: str) -> str:
    reversed_input = list(input[::-1])

    for i, char in enumerate(reversed_input):
        # switch the zeros with the original numbers
        if char == "0":
            reversed_input[i] = reversed_input.pop()
        # look for *
        if char == "*" and i + 2 < len(reversed_input):
            reversed_input[i + 1], reversed_input[i + 2] = (
                reversed_input[i + 2],
                reversed_input[i + 1],
            )
            reversed_input.pop(i)

    output = "".join(reversed_input)[::-1]
    return output


def test_decrypt():
    """
    Test for the decrypt function.
    """
    assert decrypt("43Ah*ck0rr0nk") == "hAck3rr4nk"
    assert decrypt("51Pa*0Lp*0e") == "aP1pL5e"
    assert decrypt("pTo*Ta*O") == "poTaTO"


test_encrypt()
test_decrypt()
