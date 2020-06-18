import pytest

# This Fixture became available to every test case. Whereever its "test_setup" is called the fixture will be executed

@pytest.fixture(scope="class")
def test_setup():
    print("I'll be executing First")
    yield
    print("I'll be executing at the Last")


@pytest.fixture()
def dataLoad():
    print("User Profile data")
    return ["Lalit", "Shejao", "lalit.shejao@gmail.com"]


@pytest.fixture(params=["chrome", "firefox", "ie"])
def crossBrowser(request):
    return request.param


# @pytest.yield_fixture()  this can be used as both startUP and tearDown method.
@pytest.yield_fixture(scope="module")
def startUpModule():
    print("Module activity Started")
    yield  # below will be act as a Teardown section
    print("Module activity Ended")


@pytest.yield_fixture()
def startUp():
    print("Test activity Started")
    yield
    print("Test activity Ended")

