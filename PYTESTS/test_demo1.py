# all the pytest files need to start with test_ or end with _test
import pytest


@pytest.fixture()
def setup():
    print("I will be executing first")
    yield
    print(" I will be executed last")


@pytest.mark.good
def test_pantelis():
    msg = "ah gamhsou"
    assert msg == "ah gamhsou","The test failed"


def test_pantelis2():
     msg = "kapota"
     assert msg == "kopota", "The test failed"

