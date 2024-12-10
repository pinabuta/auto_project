import sys
import os

# Добавляем полный путь к папке src в sys.path
sys.path.insert(0, '/Users/ira/PycharmProjects/ProjectAuto/src')

import src.calc
#ADD TESTS
def test_add_positive_numbers():
    assert calc.add(2, 3) == 5


def test_add_negative_numbers():
    assert calc.add(-2, -3) == -5


def test_add_mixed_numbers():
    assert calc.add(2, -3) == -1


#SUBTRACT TESTS
def test_subtract_positive_numbers():
    assert calc.subtract(2, 3) == -1


def test_subtract_negative_numbers():
    assert calc.subtract(-2, -3) == 1


def test_subtract_mixed_numbers():
    assert calc.subtract(2, -3) == 5
