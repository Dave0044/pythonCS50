from bank import value

def test_value_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0

def test_value_h_and_not_hello():
    assert value("hola34") == 20
    assert value("happiness") == 20
    assert value("H23") == 20

def test_value_other():
    assert value("python") == 100
    assert value("goodbye") == 100
    assert value("123._/") == 100
