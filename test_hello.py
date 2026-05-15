from hello import add, multiply

def test_add():
    assert add(1,2) == 3

def test_multiply():
   assert multiply(-3,2) == -6
