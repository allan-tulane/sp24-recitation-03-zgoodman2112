from main import *



## Feel free to add your own tests here.
def test_multiply():
    assert quadratic_multiply(BinaryNumber(3), BinaryNumber(3)) == 3*3
    assert quadratic_multiply(BinaryNumber(7), BinaryNumber(7)) == 7*7
    assert quadratic_multiply(BinaryNumber(3), BinaryNumber(7)) == 3*7
    assert quadratic_multiply(BinaryNumber(11), BinaryNumber(4)) == 11*4
    assert quadratic_multiply(BinaryNumber(17), BinaryNumber(38)) == 17*38
    assert quadratic_multiply(BinaryNumber(68), BinaryNumber(421)) == 68*421


