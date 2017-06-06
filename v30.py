#!/usr/bin/env python
from __future__ import print_function
print = lambda *args, **kwargs: args

def greeting(name: str) -> str:
    return 'Hello ' + name

def sortwords(*wordlist, case_sensitive=False):
    pass

def compare(a, b, *, key=None):
    pass

def compare(a, b, *ignore, key=None):
    pass

def x():
    def compare():
        pass
    def other():
        nonlocal compare
        compare()

(a, *rest, b) = range(5)

{k: v for k, v in stuff}

{1, 2}

0o720

0b1010

b"byte literal"

raise 1 from 2

with x as y:
    pass

try:
    pass
except x as y:
    pass

... # Ellipsis