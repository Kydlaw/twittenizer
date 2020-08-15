import pytest

from twittenizer.tokenizer import Tokenizer


@pytest.fixture
def tokenizer():
    from twittenizer.tokenizer import Tokenizer

    return Tokenizer()


def test_tokenize_url_1(tokenizer):
    s1 = "Here is my website: https://t.co/EZWeDhjl, check it out! "
    assert " ".join(tokenizer.tokenize(s1)) == "Here is my website check it out"


def test_tokenize_url_2(tokenizer):
    s1 = "Here is my http site!!!! mysite.com, check it out! "
    assert (
        " ".join(tokenizer.tokenize(s1))
        == "Here is my http site mysite com check it out"
    )


def test_tokenize_2(tokenizer):
    s2 = "RT @breakingstorm: Colorado's High Park Fire grows to 20,000 acres as hundreds flee - @denverpost http://t.co/ixR6bC3r"
    assert (
        " ".join(tokenizer.tokenize(s2))
        == "<RT> <USER> Colorados High Park Fire grows to <NUM> acres as hundreds flee <USER> <URL>"
    )


def test_tokenize_3(tokenizer):
    s3 = "Video: 6/10: Containing Colorado's wildfire; revisiting Watergate http://t.co/EZWeDhjl #FollowBack"
    assert (
        " ".join(tokenizer.tokenize(s3))
        == "Video <NUM> <NUM> Containing Colorados wildfire revisiting Watergate FollowBack"
    )


def test_tokenize_4(tokenizer):
    s4 = "It is doingsome raining #onthefarm!!!   LORD send of this to put out the fires in Colorado.  #Thrutheflames safety!!!  "
    assert (
        " ".join(tokenizer.tokenize(s4))
        == "It is doingsome raining <HASH> LORD send of this to put out the fires in Colorado <HASH> safety"
    )
