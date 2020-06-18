import pytest


@pytest.mark.run(order=2)
def test_m1():
    print("TestCase M1 activity")


@pytest.mark.run(order=3)
def test_m2():
    print("TestCase M2 activity")


@pytest.mark.run(order=1)
def test_m3():
    print("TestCase M3 activity")

