import pytest

@pytest.mark.usefixtures("dataLoad")
class TestExampleData:

    def test_editprof(self, dataLoad):
        print(dataLoad)

