import pytest


@pytest.mark.usefixtures("test_setup")
class TestFixture:
    def test_teardown(self):
        print("I'll be executed in between - teardown")

    def test_teardown2(self):
        print("I'll be executed in between - teardown2")

    def test_teardown3(self):
        print("I'll be executed in between - teardown3")

    def test_teardown4(self):
        print("I'll be executed in between - teardown4")

