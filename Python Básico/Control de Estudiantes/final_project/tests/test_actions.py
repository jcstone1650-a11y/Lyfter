import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from actions import (
    is_valid_name, 
    is_valid_section, 
    is_valid_grade,
    calculate_average, 
    student_exists, 
)

def test_student_exists():
    students = [
        {
            "name": "Juan Perez",
            "section": "11B",
            "grades": {
                "Spanish": 90,
                "English": 80,
                "Social Studies": 85,
                "Science": 95
            }
        }
    ]

    assert student_exists(students, "Juan Perez", "11B")

def test_student_not_exists():
    students = [
        {
            "name": "Juan Perez",
            "section": "11B",
            "grades": {
                "Spanish": 90,
                "English": 80,
                "Social Studies": 85,
                "Science": 95
            }
        }
    ]

    assert not student_exists(students, "Maria Lopez", "10A")