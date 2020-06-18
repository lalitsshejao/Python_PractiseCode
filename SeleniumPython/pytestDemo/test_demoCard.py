import pytest

def test_firstprogram():
    print("Hello World")

@pytest.mark.smoke
def test_MathCreditCard(test_setup):
    a= 4
    b = 7
    assert a + 3== b , "Error in MathCreditCard"
