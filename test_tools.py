# test_tools.py

from tools.numbers.simp import add, subtract
from tools.numbers.comp import sumofdigits, ispal
from tools.col import myzip

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    print("add function passed all tests.")

def test_subtract():
    assert subtract(2, 1) == 1
    assert subtract(-1, -1) == 0
    assert subtract(0, 0) == 0
    print("subtract function passed all tests.")

def test_sumofdigits():
    assert sumofdigits(123) == 6
    assert sumofdigits(234) == 9
    assert sumofdigits(0) == 0
    print("sumofdigits function passed all tests.")

def test_ispal():
    assert ispal(1221) == True
    assert ispal(12321) == True
    assert ispal(123) == False
    print("ispal function passed all tests.")

def test_myzip():
    assert myzip([1, 2, 3], ['a', 'b', 'c']) == [(1, 'a'), (2, 'b'), (3, 'c')]
    assert myzip([1, 2], ['a', 'b', 'c']) == [(1, 'a'), (2, 'b')]
    assert myzip([], ['a', 'b', 'c']) == []
    print("myzip function passed all tests.")

def main():
    # Call simp functions to allow usage of comp functions
    add(0, 0)

    test_add()
    test_subtract()
    test_sumofdigits()
    test_ispal()
    test_myzip()

if __name__ == "__main__":
    main()
