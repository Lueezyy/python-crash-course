import pytest
from employee import Employee

@pytest.fixture
def testemployee():
    testemployee = Employee('Luis', 'Doe', 100000)
    return testemployee

def test_give_default_raise(testemployee):
    testemployee.give_raise()
    assert testemployee.salary == 105000

def test_give_custom_raise(testemployee):
    testemployee.give_raise(1000)
    assert testemployee.salary == 101000