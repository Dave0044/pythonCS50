from um import count

def test_single_occurrence():
    assert count("hello, um, world") == 1

def test_no_occurrence():
    assert count("yummy") == 0

def test_multiple_occurrences():
    assert count("Um, um, um, excuse me") == 3

def test_case_insensitivity():
    assert count("UM, uM, Um, um") == 4
