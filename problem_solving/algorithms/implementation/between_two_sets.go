package main

func getTotalX(a []int32, b []int32) int32 {
	// Assuming that a and b are ordered
	aMax := a[len(a)-1]
	bMin := b[0]

	set := make(map[int32]bool)

	for i := aMax; i <= bMin; i = i + aMax {
		set[i] = true
	}

	for item := range set {
		// Check if matches 1st condition
		for _, aItem := range a[:len(a)-1] {
			if !(item%aItem == 0) {
				delete(set, item)
			}
		}

		// Check if matches 2nd condition
		for _, bItem := range b {
			if !(bItem%item == 0) {
				delete(set, item)
			}
		}
	}

	return int32(len(set))
}
