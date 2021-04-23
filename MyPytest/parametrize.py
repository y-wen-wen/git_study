import pytest
def add_function(a,b):
    return a+b


def test_add1():
    assert add_function(1,1) == 2
def test_add2():
    assert add_function(-1,1) == 0
def test_add3():
    assert add_function(-1,-1) == -2
def test_add4():
    assert add_function(1000000,1000000) == 2000000

