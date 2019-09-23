s = {10,20,30}

print("Type is: ",type(s))
s.add(40)
print(s)


f = frozenset(s)
print("Type is: ",type(f))
f.add(60)
print(f)
