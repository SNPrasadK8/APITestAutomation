import pytest


@pytest.fixture(scope="module") #Executes start and end of module
def fixture_code():
    print("This is the fixture before testing execution")
    print("+++++++++++++++++++++++")

    yield
    print("This is the fixture after testing execution")
    print("+++++++++++++++++++++++")


@pytest.mark.Smoke
def test_tc_003_Login_Logout_Testing(fixture_code):
    print("Third test case")