import pytest
from gradebook import letter_grade, is_passing

def test_letter_grade_A():
    assert letter_grade(95) == "A"

def test_letter_grade_F():
    assert letter_grade(50) == "F"

@pytest.mark.parametrize("score, expected", [
    (95, "A"),
    (50, "F")
])
def test_letter_grade(score, expected):
    assert letter_grade(score) == expected

def test_letter_grade_invaild_type():
    with pytest.raises(TypeError):
       letter_grade("hello")

# Testing is_passing function --------------------------------
def test_is_passing_true():
    assert is_passing(75) == True

def test_is_passing_false():
    assert is_passing(50) == False