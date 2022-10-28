from cipher_jer2240 import cipherpkg
import pytest

def test_word():
    example = 'word'
    shift = 4
    expected = 'Asvh'
    actual = cipherpkg.cipher(example, shift)
    assert actual == expected

def test_neg():
    test_text = "The New York Mets were once good at baseball and then they sucked"
    example_shift = -2
    expected = "Rfc Lcu Wmpi Kcrq ucpc mlac emmb Yr ZYqcZYjj Ylb rfcl rfcw qsaicb"
    actual = cipherpkg.cipher(test_text, example_shift)
    assert actual == expected


def test_special():
    test_text = "UhOh!?!%"
    test_shift = 5
    expected = "ZmTm!?!%"
    actual = cipherpkg.cipher(test_text, test_shift)
    assert expected == actual


