def gen():
    yield 1
    yield 2

def func():
    yield from gen()
