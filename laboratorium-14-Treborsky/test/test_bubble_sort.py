"""Bubble sort test suite"""

from bubble_sort import bubble_sort

import pytest

sorted_array = [0,1,2,3,4,5,6,7,8,9]

testdata = [
        ([0,1,2,3,4,5,6,7,8,9], sorted_array), # sorted already
        ([9,8,7,6,5,4,3,2,1,0], sorted_array), # unsorted
        ([], []), # empty
        ([4,6,8,7,9,1,3,2,0,5], sorted_array)  # random
]

@pytest.mark.parametrize('input_array, output_array', testdata)
def test_bubble_sort(input_array, output_array):

    bubble_sorted = bubble_sort(input_array)

    assert bubble_sorted == output_array

