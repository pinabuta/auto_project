from src import calc

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

#MULTIPLY TESTS
def test_multiply_positive_numbers():
    assert calc.multiply(2, 3) == 6


def test_multiply_negative_numbers():
    assert calc.multiply(-2, -3) == 6


def test_multiply_mixed_numbers():
    assert calc.multiply(2, -3) == -6

#DIVIDE TESTS
def test_divide_positive_numbers():
    assert calc.divide(3, 3) == 1


def test_divide_negative_numbers():
    assert calc.divide(-3, -3) == 1


def test_divide_mixed_numbers():
    assert calc.divide(3, -3) == -1