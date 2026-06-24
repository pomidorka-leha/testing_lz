import pytest
from testt import logarifm

if logarifm(1,5,2) == 5:
    print('true')
else :
    print('false')

if logarifm(0.000001,1,2) <0:
    print('true')
else :
    print('false')    

if logarifm(1,1,1) == True:
    print('true')
else :
    print('false')

if logarifm(1, 5, 1) == 0:
    print('true')
else :
    print('false')

if logarifm(5, 5, 1) == 1 :
    print('true')
else :
    print('false')
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^РУЧНЫЕ ТЕСТЫ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


def test_1():
    
    assert logarifm(1, 5, 2) == 5

def test_2():
    
    assert logarifm(0.000001,1,2) <0

def test_3():
    
    assert logarifm(1,1,1) == True

def test_4():

    assert logarifm(1, 5, 1) == 0       
       
def test_5():

    assert logarifm(5, 5, 1) == 1  
