import numb3rs


def test_valid_ipv4_address():
    assert numb3rs.validate("192.168.0.1") == True
    assert numb3rs.validate("10.0.0.255") == True
    assert numb3rs.validate("172.16.0.0") == True


def test_invalid_ipv4_address():
    assert numb3rs.validate("256.0.0.1") == False
    assert numb3rs.validate("192.168.0.300") == False
    assert numb3rs.validate("abc.def.ghi.jkl") == False


def test_invalid_format():
    assert numb3rs.validate("192.168.0") == False
    assert numb3rs.validate("192.168.0.1.2") == False
    assert numb3rs.validate("192.168..1") == False


if __name__ == "__main__":
    test_valid_ipv4_address()
    test_invalid_ipv4_address()
    test_invalid_format()
    print("All tests passed.")
