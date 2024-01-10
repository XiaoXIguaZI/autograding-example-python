import hello

def test_hello():
    hello.hello_world
    assert hello.hello_world() == "Hello, World!"
