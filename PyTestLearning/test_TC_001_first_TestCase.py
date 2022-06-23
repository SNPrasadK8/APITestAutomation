import pytest
actualresult = "testing"
a = 101
@pytest.mark.skipif(a>100, reason = "Skipping for testing")
def test_tc_001_Login_Logout_Testing():
    print("First Test case")



@pytest.mark.Smoke
@pytest.mark.NonSmoke
def test_tc_003_Login_Logout_Testing_Invalid_Credentials():
    print("Third Test case")
    assert actualresult == "testing"