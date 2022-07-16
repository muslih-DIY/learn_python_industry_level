
from  calculator import calculator
import pytest

def test_add(firstNumber):
    assert calculator.add(firstNumber,3 ) == 13
   
def test_sub(firstNumber):
    assert calculator.sub(firstNumber,3 ) == 7
def test_mul(firstNumber):
    assert calculator.mul(firstNumber,3 ) == 30

def test_div(firstNumber):
    assert calculator.div(firstNumber,2 ) == 5

def test_div_by_zero(firstNumber):

    assert calculator.div(firstNumber,0) == 0 


@pytest.mark.parametrize("secondNo,output", [(5,2),(10,1),(4,2.5)])
def test_div_para(firstNumber,secondNo,output):
    assert calculator.div(firstNumber,secondNo) == output 