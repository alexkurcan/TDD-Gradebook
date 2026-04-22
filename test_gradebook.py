import pytest
from gradebook import letter_grade, is_passing, average, curved_score

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

def test_is_passing_invaild_type():
    with pytest.raises(TypeError):
        is_passing("blah")

# Testing average function -----------------------------------
def test_average_works():
    assert average([80, 90, 70]) == 80.0

def test_average_empty_list():
    with pytest.raises(ValueError):
        average([])

def test_average_not_a_list():
    with pytest.raises(TypeError):
        average("Not a list..")

def test_avergae_bad_items():
    with pytest.raises(TypeError):
        average([80, "ninety", 70])

# Testing curved_score function ------------------------------
def test_curved_score_basic():
    assert curved_score(80, 5) == 85

def test_curved_score_cap():
    assert curved_score(95, 10) == 100

def test_curved_score_negative_bonus():
    with pytest.raises(WalueError):
        curved_score(80, -5)