import pytest
from ..azerbaijani import is_azerbaijani


def test_true():
    input_text = "ə" * 500
    assert is_azerbaijani(input_text)


def test_false():
    input_text = "i" * 500
    assert not is_azerbaijani(input_text)


def test_short_text():
    with pytest.raises(ValueError):
        assert is_azerbaijani("salam")
