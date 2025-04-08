"""Testing The Dictionary"""

__author__: str = "730746714"

from exercises.ex03.dictionary import invert, favorite_color, count, bin_len
import pytest

"""Unit Tests for Invert"""


# Use Cases
def test_invert_0() -> None:
    assert invert({"a": "b", "c": "d", "e": "f"}) == {"b": "a", "d": "c", "f": "e"}


def test_invert_1() -> None:
    assert invert(
        {"John": "Doe", "Jane": "Smith", "Elliot": "Cadeau", "RJ": "Davis"}
    ) == {"Doe": "John", "Smith": "Jane", "Cadeau": "Elliot", "Davis": "RJ"}


# Edge Cases
def test_invert_2() -> None:
    assert invert({}) == {}


def test_invert_3() -> None:
    with pytest.raises(KeyError):
        my_dictionary = {"Lebron": "James", "Bronny": "James"}
        invert(my_dictionary)


"""Unit Tests for Count"""


# Use Cases
def test_count_0() -> None:
    assert count(
        ["Hamburger", "Hamburger", "Hamburger", "Hotdog", "Hotdog", "Fries"]
    ) == {"Hamburger": 3, "Hotdog": 2, "Fries": 1}


def test_count_1() -> None:
    assert count(["Cat", "Dog", "Parrot", "Turtle", "Bunny", "Fish", "Bunny"]) == {
        "Cat": 1,
        "Dog": 1,
        "Parrot": 1,
        "Turtle": 1,
        "Bunny": 2,
        "Fish": 1,
    }


# Edge Case:
def test_count_2() -> None:
    count([]) == {}


"""Unit Tests for favorite_color"""


# Use Cases:
def test_favorite_color_0() -> None:
    assert (
        favorite_color(
            {
                "John": "Yellow",
                "James": "Yellow",
                "Jeffery": "Green",
                "Jolante": "Blue",
                "Jarquavion": "Yellow",
            }
        )
        == "Yellow"
    )


def test_favorite_color_1() -> None:
    assert (
        favorite_color(
            {"a": "Green", "b": "Green", "c": "Brown", "d": "Magenta", "e": "Brown"}
        )
        == "Green"
    )


# Edge Cases: Entirely Unique Values, stress-testing tie functionality
def test_favorite_color_2() -> None:
    assert (
        favorite_color(
            {
                "a": "Red",
                "b": "Orange",
                "c": "Yellow",
                "d": "Green",
                "e": "Blue",
                "f": "Violet",
            }
        )
        == "Red"
    )


"""Unit Test for bin_len"""


# Use Cases
def test_bin_len_0() -> None:
    assert bin_len(["cat", "dog", "ferret"]) == {3: {"cat", "dog"}, 6: {"ferret"}}


def test_bin_len_1() -> None:
    assert bin_len(["the", "quick", "fox"]) == {3: {"the", "fox"}, 5: {"quick"}}


# Edge Case: Repeating words of same length and value
def test_bine_len_2() -> None:
    assert bin_len(["the", "the", "fox"]) == {3: {"the", "fox"}}
