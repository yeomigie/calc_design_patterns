from commands import SumCommand, DifferenceCommand, ProductCommand, QuotientCommand

def test_sum():
    sum_cmd = SumCommand()
    assert sum_cmd.execute(2, 3) == 5

def test_difference():
    diff_cmd = DifferenceCommand()
    assert diff_cmd.execute(5, 3) == 2

def test_product():
    prod_cmd = ProductCommand()
    assert prod_cmd.execute(2, 3) == 6

def test_quotient():
    quot_cmd = QuotientCommand()
    assert quot_cmd.execute(6, 3) == 2
    try:
        quot_cmd.execute(1, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero"
