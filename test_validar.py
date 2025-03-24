from validar import validate

def test_rut():
    assert validate("11111111-1") == True