import numb3rs


def test_validate_valid_ipv4():
    assert numb3rs.validate("192.168.0.1") == True
    assert numb3rs.validate("255.255.255.255") == True


def test_validate_invalid_ipv4():
    assert numb3rs.validate("275.3.6.28") == False
    assert numb3rs.validate("192.168.0.300") == False


def test_validate_invalid_format():
    assert numb3rs.validate("not_an_ip_address") == False
    assert numb3rs.validate("192.168.0") == False
