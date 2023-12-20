package main

import (
	"testing"
)

// TestGetTotalX is a test function for getTotalX
func TestGetTotalX(t *testing.T) {
	tests := []struct {
		name     string
		a        []int32
		b        []int32
		expected int32
	}{
		{
			name:     "Test 1",
			a:        []int32{2, 6},
			b:        []int32{24, 36},
			expected: 2,
		},
		{
			name:     "Test 2",
			a:        []int32{3, 4},
			b:        []int32{24, 48},
			expected: 2,
		},
		{
			name:     "Test 3",
			a:        []int32{2, 4},
			b:        []int32{16, 32, 96},
			expected: 3,
		},
	}

	for _, tc := range tests {
		t.Run(tc.name, func(t *testing.T) {
			if got := getTotalX(tc.a, tc.b); got != tc.expected {
				t.Errorf("getTotalX(%v, %v) = %v; want %v", tc.a, tc.b, got, tc.expected)
			}
		})
	}
}
