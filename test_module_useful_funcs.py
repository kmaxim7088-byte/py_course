import pytest
import module_useful_funcs as m

# m.is_even
def test_is_even_40_true():
    assert m.is_even(40) == True


def test_is_even_1_false():
    assert m.is_even(1) == False


def test_is_even_neg_1_fasle():
    assert m.is_even(-1) == False


def test_is_even_neg_8_true():
    assert m.is_even(8) == True


# m.my_pow
def test_my_pow_2_true():
    assert m.my_pow(2) == 4

def test_my_pow_5_false():
    assert m.my_pow(5) != 4

# m.nameUpper
def test_nameUpper_true():
    assert m.nameUpper("ssddsd") == "SSDDSD"

def test_nameUpper_false():
    assert m.nameUpper("ssddsd") != "SSdDSD"