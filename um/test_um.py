from um import count
import re
import pytest

def test_um():
    assert count('um um um. um, um-') == 5
    assert count('um?') == 1
    assert count('Um, thanks for the album.') == 1
    assert count('Um, thanks, um...') == 2

def test_um_partofword():
    assert count('Number, umbrella, bumblebee') == 0