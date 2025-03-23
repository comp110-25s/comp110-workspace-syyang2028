"""Testing The Dictionary"""

__author__: str = "730746714"

from exercises.ex03.dictionary import favorite_color

# """Unit Test for invert"""
# from excercises.ex03.dictionary import invert

# Use Case
# Use Case
# Edge Case

# """Unit Test for count"""
# from exercises.ex03.dictionary import count

# Use Case
# Use Case
# Edge Case


"""Unit Test for favorite_color"""

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

# Use Case
# Use Case
# Edge Case


# """Unit Test for bin_len"""
# from exercises.ex03.dictionary import bin_len

# Use Case
# Use Case
# Edge Case


# python -m pytest exercises/ex03
