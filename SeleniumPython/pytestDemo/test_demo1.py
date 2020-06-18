import pytest

@pytest.mark.smoke
@pytest.mark.skip
def test_demo():
    a = "Hello How Are You"
    assert a == "Hi", "Assertion Failed in GreetingCreditCard"

@pytest.mark.xfail
def test_GreetingCreditCard(test_setup):
    a= "Hello How Are You"
    assert a == "Hello How Are You", "Assertion Failed in GreetingCreditCard"
