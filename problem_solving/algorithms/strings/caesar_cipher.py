def caesar_cipher(cleartext_input, k):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letter_positions = {}
    for index, letter in enumerate(alphabet):
        letter_positions[letter] = index

    encrypted_output = ""
    for char in cleartext_input:
        if char.lower() in alphabet:
            is_lowercase = char.lower() == char
            if is_lowercase:
                encrypted_output += alphabet[
                    (letter_positions[char.lower()] + k) % 26
                ]
            else:
                encrypted_output += alphabet[
                    (letter_positions[char.lower()] + k) % 26
                ].upper()
        else:
            encrypted_output += char

    return encrypted_output


def test_caesar_cipher():
    """Test for caesar_cipher function."""
    assert caesar_cipher("middle-Outz", 2) == "okffng-Qwvb"
    assert (
        caesar_cipher("Always-Look-on-the-Bright-Side-of-Life", 5)
        == "Fqbfdx-Qttp-ts-ymj-Gwnlmy-Xnij-tk-Qnkj"
    )


test_caesar_cipher()
