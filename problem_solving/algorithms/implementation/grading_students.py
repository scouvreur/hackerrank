#!/bin/python3

from typing import List


def round_grade(grade: int) -> int:
    """
    Round the grade according to policy.

    Parameters
    ----------
    grade: int
        Raw grade.

    Returns
    -------
    rounded_grade: int
        Rounded grade.
    """
    if grade < 38:
        rounded_grade = grade
    else:
        closest_multiple_5 = (grade // 5 + 1) * 5
        if (closest_multiple_5 - grade) >= 3:
            rounded_grade = grade
        else:
            rounded_grade = closest_multiple_5
    return rounded_grade


def grading_students(grades: List[int]) -> List[int]:
    """
    Complete the grading_students function below.

    Parameters
    ----------
    grades: List[int]
        Array of integers with the grades.

    Returns
    -------
    rounded_grades: List[int]
        Array of integers with rounded grades.
    """
    rounded_grades = []
    for grade in grades:
        rounded_grades.append(round_grade(grade))
    return rounded_grades


def test_round_grade():
    """Test for round_grade function."""
    assert round_grade(grade=73) == 75
    assert round_grade(grade=67) == 67
    assert round_grade(grade=38) == 40
    assert round_grade(grade=33) == 33


def test_grading_students():
    """Test for grading_students function."""
    assert grading_students(grades=[84]) == [85]
    assert grading_students(grades=[29]) == [29]
    assert grading_students(grades=[57]) == [57]
    assert grading_students(grades=[73, 67, 38, 33]) == [
        75,
        67,
        40,
        33,
    ]


test_grading_students()
grades_count = int(input().strip())
grades = []
for _ in range(grades_count):
    grades_item = int(input().strip())
    grades.append(grades_item)

result = grading_students(grades)
for grade in result:
    print(grade)
