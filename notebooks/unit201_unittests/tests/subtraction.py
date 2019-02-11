from student_solutions import *
from hypothesis import given, settings
import hypothesis.strategies as st


@given(number1=st.integers(),
       number2=st.integers())
@settings(max_examples=10000)
def test_subtraction(number1, number2):
    assert number1 - number2 == subtraction(number1, number2)
