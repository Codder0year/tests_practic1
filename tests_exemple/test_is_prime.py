from scr.is_prime import is_prime
def test_is_prime():
    number = 8
    result = False
    number_two = 7
    result_two = True

    assert is_prime(number) == result
    assert is_prime(number_two) == result_two
