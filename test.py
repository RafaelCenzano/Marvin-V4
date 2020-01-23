import pathlib
import os
p = pathlib.Path()
q = pathlib.Path('.')
r = pathlib.Path(__file__)
s = pathlib.Path('test.py')

print(p)
print(q)
print(r)
print(s)
print(p.resolve())
print(q.resolve())
print(r.resolve())
print(s.resolve())
print(pathlib.Path.cwd())
print(__file__)