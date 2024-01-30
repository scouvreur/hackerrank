package implementation

import (
	"testing"
)

func TestEncryption(t *testing.T) {
	testCases := []struct {
		input    string
		expected string
	}{
		{
			input:    "if man was meant to stay on the ground god would have given us roots",
			expected: "imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn sseoau",
		},
		{
			input:    "have a nice day",
			expected: "hae and via ecy",
		},
		{
			input:    "feed the dog",
			expected: "fto ehg ee dd",
		},
		{
			input:    "chill out",
			expected: "clu hlt io",
		},
	}

	for _, tc := range testCases {
		result := encryption(tc.input)
		if result != tc.expected {
			t.Errorf("Expected %q, but got %q", tc.expected, result)
		}
	}
}
